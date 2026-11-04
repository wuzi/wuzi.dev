# Imported content and asset provenance

Imported on 2026-11-04 from [`wuzi/blog` at `a19bf18aa7670e5090926f1c128b4a1008645fb0`](https://github.com/wuzi/blog/tree/a19bf18aa7670e5090926f1c128b4a1008645fb0). The source Git tree supplied the expected blob hashes and lengths; every imported file matched both before it was copied. Downloads used that immutable commit, not a branch name.

[`tests/migration.json`](../tests/migration.json) records the independent migration baseline: original Markdown SHA-256 hashes, ordered media paths, titles and UTC publication timestamps, 17 static-file hashes and lengths, the original project-data hash, feed GUIDs, pagination aliases, and deliberately retired routes. These are source and legacy-site expectations, not values derived from the new generated site. Update them only when an intentional content change has been approved and reviewed.

## Editorial content

These two files were copied byte-for-byte, retaining their original filename casing, wording, front matter, whitespace, image order, and the unlabelled maze code block:

| Source file | Published route | Published timestamp |
| --- | --- | --- |
| [`content/posts/history-of-labirong.md`](https://github.com/wuzi/blog/blob/a19bf18aa7670e5090926f1c128b4a1008645fb0/content/posts/history-of-labirong.md) | `/posts/history-of-labirong/` | `2022-05-03T17:06:00Z` |
| [`content/posts/creating-a-2D-game-including-all-the-assets-part-1.md`](https://github.com/wuzi/blog/blob/a19bf18aa7670e5090926f1c128b4a1008645fb0/content/posts/creating-a-2D-game-including-all-the-assets-part-1.md) | `/posts/creating-a-2d-game-including-all-the-assets-part-1/` | `2021-07-11T23:30:00Z` |

The source front matter has no explicit timezone; the UTC timestamps above preserve the legacy site's published timestamps. The uppercase `2D` stays in the source filename while its published route stays lowercase.

All 11 article images were copied from the source's `static/images/` directory to the same relative paths. No recompression, resizing, conversion, or animation flattening was performed:

| Article | Image paths in original reading order |
| --- | --- |
| History of Labirong | `/images/history-of-labirong/maze-version-0.png`, `/images/history-of-labirong/maze-version-1.png`, `/images/history-of-labirong/maze-version-2.png`, `/images/history-of-labirong/maze-version-3.png`, `/images/history-of-labirong/maze-version-4.png`, `/images/history-of-labirong/labirongo.png`, `/images/history-of-labirong/labirong3d.png` |
| Creating a 2D game | `/images/woltileset.jpg`, `/images/character.jpg`, `/images/charactersheet.gif`, `/images/final.gif` |

`charactersheet.gif` retains 152 frames and `final.gif` retains 106 frames. The two posts and their included images remain attributed as they were in Wuzi's source. The Labirong article's existing acknowledgement of the author's brother and free online sprites remains intact; this migration does not add a new license or an authorship claim over those underlying game assets.

The complete [`data/projects.json`](https://github.com/wuzi/blog/blob/a19bf18aa7670e5090926f1c128b4a1008645fb0/data/projects.json) was also copied byte-for-byte. Its original `{"list": [...]}` shape, 17 entries, order, names, URLs, descriptions, capitalization, and historical years are unchanged. These descriptions are historical source content, not a new claim of current project activity.

## Retained stock artwork

The existing stock Cactus illustration and favicon were explicitly retained for this site:

| Destination | Original source |
| --- | --- |
| `static/images/logo.png` | [`static/images/logo.png`](https://github.com/wuzi/blog/blob/a19bf18aa7670e5090926f1c128b4a1008645fb0/static/images/logo.png) |
| `static/images/favicon.ico` | [`themes/cactus/static/images/favicon.ico`](https://github.com/wuzi/blog/blob/a19bf18aa7670e5090926f1c128b4a1008645fb0/themes/cactus/static/images/favicon.ico) |
| `static/images/LICENSE-Cactus.txt` | [`themes/cactus/LICENSE`](https://github.com/wuzi/blog/blob/a19bf18aa7670e5090926f1c128b4a1008645fb0/themes/cactus/LICENSE) |

The top-level logo and the bundled theme's logo have identical Git blob hashes (`f4a9dac1a38da670b5ee5cc9304f2d786f389982`). They are stock theme artwork, not a new custom Wuzi illustration. The bundled MIT notice, copyright (c) 2020 ZERAN WU, is preserved in full at [`static/images/LICENSE-Cactus.txt`](../static/images/LICENSE-Cactus.txt). The source [`theme.toml`](https://github.com/wuzi/blog/blob/a19bf18aa7670e5090926f1c128b4a1008645fb0/themes/cactus/theme.toml) attributes the Hugo theme to Zeran Wu and the original Hexo Cactus theme to Pieter Robberechts. The new site has no Cactus theme dependency.

## Self-hosted fonts

The original JetBrains Mono Regular and Bold WOFF2 files were reused byte-for-byte from the pinned source. Font metadata identifies the family as JetBrains Mono, styles Regular and Bold, foundry `JB`, font version 1.0. The original accompanying Apache License 2.0 is retained unchanged; no newer font release or license was substituted.

| Destination | Original source |
| --- | --- |
| `static/fonts/JetBrainsMono-Regular.woff2` | [`themes/cactus/static/lib/JetBrainsMono/web/woff2/JetBrainsMono-Regular.woff2`](https://github.com/wuzi/blog/blob/a19bf18aa7670e5090926f1c128b4a1008645fb0/themes/cactus/static/lib/JetBrainsMono/web/woff2/JetBrainsMono-Regular.woff2) |
| `static/fonts/JetBrainsMono-Bold.woff2` | [`themes/cactus/static/lib/JetBrainsMono/web/woff2/JetBrainsMono-Bold.woff2`](https://github.com/wuzi/blog/blob/a19bf18aa7670e5090926f1c128b4a1008645fb0/themes/cactus/static/lib/JetBrainsMono/web/woff2/JetBrainsMono-Bold.woff2) |
| `static/fonts/LICENSE-JetBrainsMono.txt` | [`themes/cactus/static/lib/JetBrainsMono/LICENSE`](https://github.com/wuzi/blog/blob/a19bf18aa7670e5090926f1c128b4a1008645fb0/themes/cactus/static/lib/JetBrainsMono/LICENSE) |

Font files are served locally under `/fonts/`; no third-party font request is required.

## Legacy compatibility evidence

On 2026-11-04, all 13 imported image files and both font files also matched their live `https://wuzi.dev` equivalents by SHA-256. The 11 editorial image lengths matched the earlier live audit. There were no byte differences. The original live font paths were `/lib/JetBrainsMono/web/woff2/JetBrainsMono-Regular.woff2` and `/lib/JetBrainsMono/web/woff2/JetBrainsMono-Bold.woff2`; only their local destination changes.

The eight feed expectations retain existing absolute `https://wuzi.dev/` GUIDs. `/tags/index.xml` and `/categories/index.xml` contain taxonomy terms. The home, posts, tag-term, and category-term feeds contain articles. The four term feeds and six `/page/1/` aliases were checked against the live site in addition to the prior audit.

The stale `test` placeholder family is listed explicitly in the migration manifest for retirement. No content was imported from the stale `public` submodule, generated output, or the bundled theme's 22 example articles. The legacy deployment script was not run.
