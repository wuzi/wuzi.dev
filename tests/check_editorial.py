#!/usr/bin/env python3
"""Exercise publication boundaries in a temporary copy, never in real content."""
from pathlib import Path
import os
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
HUGO = os.environ.get('HUGO_BIN', str(ROOT / '.tools/hugo-0.169.0/hugo'))

with tempfile.TemporaryDirectory(prefix='wuzi-editorial-') as temporary:
    target = Path(temporary)
    for name in ['content', 'static', 'assets', 'data', 'layouts', 'tests']:
        shutil.copytree(ROOT / name, target / name)
    shutil.copy2(ROOT / 'hugo.toml', target / 'hugo.toml')
    posts = target / 'content/posts'
    fixtures = [
        ('draft-fixture', 'DRAFT_SENTINEL', '2024-01-01T00:00:00Z', True),
        ('future-fixture', 'FUTURE_SENTINEL', '2999-01-01T00:00:00Z', False),
        ('approved-fixture', 'An approved A&B <example>', '2024-01-01T00:00:00Z', False),
    ]
    for slug, title, date, draft in fixtures:
        (posts / (slug + '.md')).write_text(f'---\ntitle: "{title}"\ndate: {date}\ndraft: {str(draft).lower()}\ntags: [game]\ncategories: [development]\n---\n\nA new article with an ampersand & a literal < symbol.\n')
    subprocess.run([HUGO, '--source', str(target), '--destination', str(target / 'dist'), '--environment', 'production'], check=True, capture_output=True)
    rendered = '\n'.join(p.read_text() for p in (target / 'dist').rglob('*') if p.suffix in {'.html', '.xml'})
    assert 'DRAFT_SENTINEL' not in rendered and 'draft-fixture' not in rendered, 'Draft leaked into production output'
    assert 'FUTURE_SENTINEL' not in rendered and 'future-fixture' not in rendered, 'Future post leaked into production output'
    assert (target / 'dist/posts/approved-fixture/index.html').is_file(), 'Approved post was not published'
    rss = ET.parse(target / 'dist/index.xml')
    assert any(i.findtext('title') == 'An approved A&B <example>' for i in rss.findall('./channel/item')), 'RSS did not preserve literal title characters'
    result = subprocess.run(['python3', str(target / 'tests/check_site.py')], capture_output=True, text=True)
    assert result.returncode == 0, 'Adding an approved post broke the migration contract:\n' + result.stdout + result.stderr
print('PASS: approved-post growth, XML characters, draft and future-post exclusion')
