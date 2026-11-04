# Writing as Wuzi

## Voice

The starting examples are “History of Labirong” and “Creating a 2D game including all the assets (part 1).” They are personal project journals: informal English, first person, chronological, specific, and supported by screenshots or code. They show what happened, what was difficult, and what changed. Two short posts are a starting point, not a complete model of Wuzi's voice; incorporate his corrections into this guide when asked.

Use straightforward words, natural contractions and short paragraphs. Keep a little of the conversational rhythm: “so I tried…”, “it was pretty simple…”, “just for fun.” These are examples of the tone, not phrases to repeat mechanically. Explain a concrete experiment before extracting a general lesson. Let screenshots and code carry their share of the explanation.

Lightly improve grammar and repetition in new drafts. Avoid inflated claims, marketing copy, polished motivational conclusions, artificial suspense, and generic tutorial filler. Do not rewrite the old articles to fit this guidance.

## Evidence and authorship

Ask for the project notes or experience needed for a personal story. Do not invent things Wuzi built, used, measured, believed, or learned. Clearly separate researched explanations from firsthand experience; verify changeable technical claims against primary sources. Leave factual gaps visible in the chat draft rather than filling them with fiction. Respect private project/customer/company information; include only material Wuzi supplies for publication or has already made public.

## From an idea to a post

1. Start with Wuzi's topic, goal, notes, screenshots, or code. Suggest a narrow angle if needed.
2. Draft in chat, keeping the existing posts as voice references. For a saved working draft use `.drafts/`, never the public content directory.
3. Let Wuzi review and revise it. A draft or editing request alone does not publish anything.
4. On an explicit publication instruction, add the approved article to `content/posts/` with title, UTC date, permanent lowercase slug, tags and a short description. Set `draft: false` only at that point. Bundle approved media locally.
5. Run `npm run check`, review the rendered page, commit with a lowercase subject, and publish through Sites. Confirm the published URL.

Drafts and future-dated posts are excluded from production output. The public Git repository is also a publication surface: even a `draft: true` file must not be pushed before approval.

## A useful shape

- What I wanted to make or understand.
- The first attempt, with something concrete to show.
- What changed, failed, or became interesting.
- Where the project ended up and what I might try next, when that is true.

Use this only when it fits the story. Not every post needs headings or a conclusion.
