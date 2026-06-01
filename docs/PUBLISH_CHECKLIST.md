# Publish Checklist

## EN - Static Site Pre-flight

Use this before publishing to GitHub Pages, Vercel, or any static host.

- [ ] `index.html` opens locally without console errors.
- [ ] All `img` paths under `case-folder/` resolve with no 404.
- [ ] All `a href` links under `case-folder/` resolve with no 404.
- [ ] `case-folder/beacon-geo-report/beacon-geo-example-report.pdf` opens from the Beacon GEO CTA.
- [ ] EN/JP toggle works on nav, Beacon GEO, blogs, and contact.
- [ ] `og:title` and `og:description` are present.
- [ ] `og:image` is present and uses an absolute URL. Current assumption: `https://wayneyuan33.github.io/utakata-lab/hero-illustration.png`.
- [ ] Favicon is present, or favicon gap is accepted for this publish.
- [ ] Mobile nav works at 768px and 1024px; the Beacon GEO nav item is not broken or wrapped awkwardly.
- [ ] Git status does not include unwanted gitignored collateral such as decks, schedules, audits, or local prototype HTML.
- [ ] After any PDF update, run the sync steps in `docs/GEO_MONITORING_SYNC.md`.

## JP - 公開前チェック

公開前に PDF、画像リンク、多言語切替、OG 画像、モバイルナビを必ず確認します。

## PDF CTA Check

The homepage CTA label is `Download Example Report`. It should open:

`case-folder/beacon-geo-report/beacon-geo-example-report.pdf`

A browser PDF viewer is acceptable. The requirement is that the new tab loads the PDF rather than a 404.

## Known Product Gaps

Portfolio card URLs may still use `href="#"`. Do not replace them without a separate product decision.
