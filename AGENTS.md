# Working on Wuzi Codes

- Read `docs/writing-guide.md` before drafting or editing an article.
- The two migrated articles are historical originals. Preserve their source bytes and assets unless Wuzi explicitly requests an editorial change.
- Requests for ideas or drafts do not authorize publishing. Keep unapproved writing in chat or `.drafts/` (ignored by Git), outside `content/`.
- Only after Wuzi reviews and explicitly instructs publication: add the final article to `content/posts/`, choose its permanent lowercase URL, run the checks, and follow the Sites publishing workflow.
- This repository is public. Never commit unreviewed drafts, credentials, personal notes, or environment files.
- Keep the site static and progressively enhanced. New infrastructure needs a demonstrated feature requirement.
- Use lowercase commit subjects, preserving proper nouns and identifiers. Do not post GitHub/Jira comments or reviews without explicit permission.
- Run `npm run check` before committing site changes. Visual changes also need desktop/mobile and light/dark browser inspection.
- Sites uses `.openai/hosting.json`; reuse its `project_id`. Commit source before the Sites workflow helper so its automatic commit does not change the subject capitalization.
- Never execute or modify the legacy repositories' deployment scripts.
