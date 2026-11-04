import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { runInNewContext } from 'node:vm';

function browser({ hostname = 'localhost', protocol = 'http:', stored = null, blocked = false } = {}) {
  const handlers = {}, appended = [], attrs = {};
  const button = { hidden: true, addEventListener(type, fn) { handlers[type] = fn; }, setAttribute(k, v) { attrs[k] = v; } };
  const label = { textContent: '' };
  const state = { stored };
  const document = {
    documentElement: { dataset: {} },
    readyState: 'complete',
    head: { appendChild(node) { appended.push(node); } },
    createElement(tagName) { return { tagName }; },
    getElementById(id) { return id === 'theme-toggle' ? button : label; },
    addEventListener(_type, fn) { fn(); }
  };
  const context = { document, location: { hostname, protocol },
    localStorage: {
      getItem() { if (blocked) throw new Error('Storage denied'); return state.stored; },
      setItem(_key, value) { if (blocked) throw new Error('Storage denied'); state.stored = value; },
      removeItem() { if (blocked) throw new Error('Storage denied'); state.stored = null; }
    }
  };
  context.window = context;
  return { context, document, button, label, attrs, handlers, appended, state };
}
function execute(name, target) {
  const path = resolve(`assets/js/${name}.js`);
  runInNewContext(existsSync(path) ? readFileSync(path, 'utf8') : '', target.context);
}

test('saved theme applies before page interaction and advances to system preference', () => {
  const b = browser({ stored: 'dark' }); execute('theme', b);
  assert.equal(b.document.documentElement.dataset.theme, 'dark');
  assert.equal(b.button.hidden, false);
  b.handlers.click();
  assert.equal(b.document.documentElement.dataset.theme, undefined);
  assert.equal(b.state.stored, null);
  assert.equal(b.label.textContent, 'auto');
});
test('theme remains usable when persistent storage is blocked', () => {
  const b = browser({ blocked: true }); execute('theme', b);
  assert.equal(b.button.hidden, false);
  b.handlers.click();
  assert.equal(b.document.documentElement.dataset.theme, 'light');
  b.handlers.click();
  assert.equal(b.document.documentElement.dataset.theme, 'dark');
});
test('invalid stored preference falls back to system and never creates a bogus theme', () => {
  const b = browser({ stored: 'unknown' }); execute('theme', b);
  assert.equal(b.document.documentElement.dataset.theme, undefined);
  assert.equal(b.label.textContent, 'auto');
});
test('Google Analytics loads on the final HTTPS hostname with the original measurement ID', () => {
  const b = browser({ hostname: 'wuzi.dev', protocol: 'https:' }); execute('analytics', b);
  assert.equal(b.appended.length, 1);
  assert.equal(b.appended[0].src, 'https://www.googletagmanager.com/gtag/js?id=G-QD8G5JD9HB');
  assert.equal(b.context.dataLayer[1][0], 'config');
  assert.equal(b.context.dataLayer[1][1], 'G-QD8G5JD9HB');
});
test('analytics stays inactive on local, private Sites, lookalike hosts and HTTP', () => {
  for (const [hostname, protocol] of [['localhost','http:'],['wuzi-codes.paleladybird.chatgpt.site','https:'],['wuzi.dev.example.com','https:'],['wuzi.dev','http:']]) {
    const b = browser({ hostname, protocol }); execute('analytics', b);
    assert.equal(b.appended.length, 0, hostname);
    assert.equal(b.context.dataLayer, undefined, hostname);
  }
});
