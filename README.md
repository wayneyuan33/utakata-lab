# UTAKATA LAB

UTAKATA LAB is a zero-build static homepage for an AI digital marketing lab, including the Beacon GEO featured module and bilingual writing section.

Live site: https://wayneyuan33.github.io/utakata-lab/

## What Ships

The publishable site is the tracked static root:

- `index.html` - the homepage, embedded CSS, embedded JavaScript, Beacon GEO module, and inline blog content.
- `hero-illustration.png` - hero artwork and current Open Graph image source.
- `case-folder/` - portfolio visuals and Beacon GEO report assets used by the page.
- `tools/` - local generation utilities; not required at runtime, but tracked for reproducible Beacon GEO assets.
- `docs/` - operational documentation for content updates, publishing, and PDF sync.

No build step is required. Static hosts should serve the repo root.

## What Stays Local

The repo intentionally keeps planning drafts and collateral out of the public release through `.gitignore`:

- Root `*-prd.md` planning files and `blog-*.md` source drafts are local working documents unless explicitly force-added.
- Sales decks, schedules, business-card PNGs, audit captures, logs, temp files, and `.claude/` are local collateral.
- Case-folder prototype HTML files are local references; the public homepage links only to shipped static assets.

Blog markdown is not deployed by itself. Public blog content lives inside `index.html`.

## Local Preview

```powershell
npx serve -p 3000 .
```

Then open `http://localhost:3000/` and test the Beacon GEO module, language toggle, and report PDF CTA.

## Directory Map

```text
/
├── index.html
├── hero-illustration.png
├── README.md
├── docs/
│   ├── INDEX.md
│   ├── CONTENT_WORKFLOW.md
│   ├── PUBLISH_CHECKLIST.md
│   └── GEO_MONITORING_SYNC.md
├── tools/
│   ├── README.md
│   └── create_beacon_geo_ads.py
└── case-folder/
    ├── beacon-geo-report/
    │   ├── beacon-geo-report-Sample-en.pdf
    │   ├── beacon-geo-ad-01-keyword-map.png
    │   ├── beacon-geo-ad-02-ai-answer-capture.png
    │   ├── beacon-geo-ad-03-visibility-metrics.png
    │   ├── beacon-geo-ad-04-report-output.png
    │   └── source-panels/
    ├── luxury-beauty-llmo-case/
    └── top-10-tech-trend-personality-test/
```

## Operations Docs

- [Documentation index](docs/INDEX.md)
- [Content workflow](docs/CONTENT_WORKFLOW.md)
- [Publish checklist](docs/PUBLISH_CHECKLIST.md)
- [Geo-monitoring PDF sync](docs/GEO_MONITORING_SYNC.md)

Related repo: `C:\dev\geo-monitoring-app` is the Beacon GEO product repo. It owns the anonymized report sample that is copied into this static HP repo for the homepage CTA.

日本語 / 中文: Start with `docs/INDEX.md` for the operating map, then use the workflow docs before editing public content.
