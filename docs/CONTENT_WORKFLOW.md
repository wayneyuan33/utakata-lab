# Content Workflow

## EN - Source of Truth

Public content ships from `index.html`. The `blog-NN-*.md` files are local source drafts only and are ignored by default.

When editing a blog post:

1. Update the matching `blog-NN-*.md` file for local editorial history.
2. Manually sync the final body into the matching `<article class="blog-post">` block in `index.html`.
3. Keep both language blocks current: `data-en` and `data-jp` text must remain paired.
4. Preview the page and test the language toggle before publishing.

Do not edit only markdown and expect deploy to update. Static hosting reads `index.html`, not the ignored markdown files.

## JP - 重要メモ

公開される本文は `index.html` 内の `<article class="blog-post">` です。`blog-*.md` だけを編集しても本番ページは変わりません。

## Display Order vs File Numbering

The page displays newest posts first:

- Blog 02 and Blog 03 appear near the top of the Writing section.
- Blog 01 is the oldest and appears lower in the list.
- File numbering remains historical source order; page order is editorial display order.

## Bilingual QA

Before publish:

- Toggle EN and JP from the nav.
- Confirm nav labels, Beacon GEO copy, blog titles, blog summaries, expanded article bodies, and contact copy switch correctly.
- Expand each blog post in both languages.
- Confirm no English-only update was added without a JP counterpart, or vice versa.

## Adding Blog Post 04

1. Add a local source file such as `blog-04-short-title.md`.
2. In `index.html`, copy the existing blog article template comment/block in the Writing section.
3. Insert the new `<article class="blog-post">` in the intended display position, usually above older posts.
4. Add `data-en` and `data-jp` versions for title, summary, CTA labels, and full body content.
5. Run local preview and the bilingual QA above.

## Related Checks

Use `docs/PUBLISH_CHECKLIST.md` before deploy.
