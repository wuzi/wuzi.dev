#!/usr/bin/env python3
"""Assert migration contracts against the generated site, not template text."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
checks = 0

def require(condition, message):
    global checks
    assert condition, message
    checks += 1

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.links, self.images, self.canonicals, self.text, self.metas = [], [], [], [], {}
        self.content_text, self.content_images = [], []
        self.depth = 0
        self.feed(path.read_text())
    def handle_starttag(self, tag, pairs):
        a = dict(pairs)
        if tag == 'div' and 'post-content' in a.get('class', '').split():
            self.depth = 1
        elif self.depth and tag not in {'img','br','hr','input','meta','link','source','wbr'}:
            self.depth += 1
        if tag == 'a' and 'href' in a: self.links.append(a['href'])
        if tag == 'img':
            self.images.append(a.get('src', ''))
            if self.depth: self.content_images.append(a.get('src', ''))
        if tag == 'link' and a.get('rel') == 'canonical': self.canonicals.append(a.get('href'))
        if tag == 'meta': self.metas[a.get('name', a.get('property', ''))] = a.get('content', '')
    def handle_endtag(self, tag):
        if self.depth: self.depth -= 1
    def handle_data(self, value):
        self.text.append(value)
        if self.depth: self.content_text.append(value)

def output(route):
    return OUT / (route.lstrip('/') + ('index.html' if route.endswith('/') else ''))

def normalize(text):
    # The original live Hugo pages already use typographic punctuation.
    # Source hashes pin the authored bytes; this compares displayed wording.
    text = text.translate(str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"', '…': '...'}))
    return re.sub(r'\s+', ' ', text).strip()

def main():
    require((OUT / 'index.html').is_file(), 'Missing generated homepage: build the site first')
    manifest = json.loads((ROOT / 'tests/migration.json').read_text())
    for post in manifest['posts']:
        source = ROOT / post['source_path']
        require(digest(source) == post['sha256'], f'Original article changed: {source.name}')
        target = output(post['route'])
        require(target.is_file(), f'Missing original URL: {post["route"]}')
        page = Page(target)
        require(page.canonicals == ['https://wuzi.dev' + post['route']], f'Wrong canonical: {post["route"]}')
        require(page.content_images == post['images'], f'Article media order/URLs changed: {post["route"]}')
        body = source.read_text().split('---', 2)[2].strip()
        body = re.sub(r'```[^\n]*\n(.*?)```', lambda m: '\n\n' + m[1] + '\n\n', body, flags=re.S)
        body = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', body)
        body = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', body)
        body = re.sub(r'(?m)^#{1,6}\s+', '', body)
        rendered = normalize(' '.join(page.content_text))
        for paragraph in re.split(r'\n\s*\n', body):
            paragraph = normalize(paragraph).replace('**', '').replace('`', '')
            if paragraph: require(paragraph in rendered, f'Article text omitted/changed: {post["route"]}: {paragraph[:70]}')
    for asset in manifest['assets']:
        path = asset['path'].lstrip('/')
        require(digest(ROOT / 'static' / path) == asset['sha256'], f'Source image changed: {path}')
        require(digest(OUT / path) == asset['sha256'], f'Built image changed: {path}')
    require(digest(ROOT / 'tests/fixtures/projects-original.json') == manifest['projects']['sha256'], 'Original project baseline changed')
    projects = json.loads((ROOT / 'data/projects.json').read_text())['list']
    originals = json.loads((ROOT / 'tests/fixtures/projects-original.json').read_text())['list']
    require({(p['name'], p['url']) for p in originals}.issubset({(p['name'], p['url']) for p in projects}), 'Original project links missing')
    require(len({p['url'].lower().rstrip('/') for p in projects}) == len(projects), 'Duplicate project URLs')
    page = Page(output('/projects/'))
    for project in projects:
        require(project['url'] in page.links, f'Missing project link: {project["name"]}')
        require(normalize(project['desc']) in normalize(' '.join(page.text)), f'Changed project description: {project["name"]}')
    articles = {'https://wuzi.dev/posts/' + p.parent.name + '/' for p in (OUT / 'posts').glob('*/index.html')}
    home = Page(OUT / 'index.html')
    require(not re.search(r'&(?:rsquo|lsquo|ldquo|rdquo|hellip);', ' '.join(home.text)), 'HTML entities leaked into visible excerpts')
    for feed in manifest['feeds']:
        path = output(feed['route'])
        require(path.is_file(), f'Missing feed: {feed["route"]}')
        root = ET.parse(path).getroot()
        items = root.findall('./channel/item')
        guids = [item.findtext('guid') for item in items]
        require(set(feed['items']).issubset(guids), f'Original RSS items missing: {feed["route"]}: {guids}')
        if feed['kind'] == 'terms':
            taxonomy = feed['route'].split('/')[1]
            expected = {'https://wuzi.dev/' + taxonomy + '/' + p.parent.name + '/' for p in (OUT / taxonomy).glob('*/index.html')}
        elif feed['route'] in ['/index.xml', '/posts/index.xml']:
            expected = articles
        else:
            archive = Page(output(feed['route'].removesuffix('index.xml')))
            expected = {'https://wuzi.dev' + link for link in archive.links if 'https://wuzi.dev' + link in articles}
        require(set(guids) == expected, f'RSS disagrees with its archive: {feed["route"]}: {guids}')
        self_link = root.find('./channel/{http://www.w3.org/2005/Atom}link')
        require(self_link is not None and self_link.attrib.get('href') == 'https://wuzi.dev' + feed['route'], f'Wrong RSS self URL: {feed["route"]}')
        for item in items:
            for post in manifest['posts']:
                if item.findtext('guid') == 'https://wuzi.dev' + post['route']:
                    from email.utils import parsedate_to_datetime
                    from datetime import datetime
                    require(parsedate_to_datetime(item.findtext('pubDate')) == datetime.fromisoformat(post['date'].replace('Z', '+00:00')), f'Changed feed date: {post["route"]}')
    for alias in manifest['aliases']:
        path = output(alias['route'])
        require(path.is_file(), f'Missing legacy alias: {alias["route"]}')
        require('https://wuzi.dev' + alias['target'] in path.read_text(), f'Wrong alias target: {alias["route"]}')
    for route in manifest['retired']:
        require(not output(route).exists(), f'Retired placeholder still published: {route}')
    require((OUT / '404.html').is_file(), 'Missing 404 page')
    sitemap = ET.parse(OUT / 'sitemap.xml').getroot()
    urls = [x.text for x in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    require(all('/test/' not in url and '/page/1/' not in url for url in urls), 'Sitemap includes aliases/placeholders')
    require(all('https://wuzi.dev' + p['route'] in urls for p in manifest['posts']), 'Sitemap missing original articles')
    require('Disallow: /' not in (OUT / 'robots.txt').read_text(), 'Production robots blocks indexing')
    for path in OUT.rglob('*.html'):
        page = Page(path)
        for link in page.links + page.images:
            if not link.startswith('/') or link.startswith('//'): continue
            route = unquote(urlsplit(link).path)
            require(output(route).exists(), f'Broken internal link in {path.relative_to(OUT)}: {link}')
        if path.name != '404.html': require('noindex' not in page.metas.get('robots', ''), f'Unexpected noindex: {path}')
    print(f'PASS: {checks} migration and generated-site assertions')

if __name__ == '__main__':
    try: main()
    except (AssertionError, FileNotFoundError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        sys.exit(1)
