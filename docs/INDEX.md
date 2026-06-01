# Documentation Index

This is the operating map for UTAKATA HP. Paths are repo-root relative.

| Document | Path | Git tracked? | Status | Notes |
|---|---|---:|---|---|
| Homepage | `index.html` | Yes | IMPLEMENTED | Public static page with Beacon GEO, blogs, nav, contact, and OG metadata. |
| Entry README | `README.md` | Yes | DONE | Preview, publishable files, local-only files, and doc links. |
| Documentation remediation spec | `docs/DOC_REMEDIATION_SPEC.md` | Yes | DONE | Approved scope for DOC-REM. |
| Documentation remediation work order | `docs/DOC_REMEDIATION_IMPLEMENT_WORK_ORDER.md` | Yes | DONE | Implementation order and REM acceptance list. |
| Content workflow | `docs/CONTENT_WORKFLOW.md` | Yes | DONE | Blog markdown to `index.html` sync and bilingual QA. |
| Publish checklist | `docs/PUBLISH_CHECKLIST.md` | Yes | DONE | Static publish checks, PDF, mobile, bilingual, OG image. |
| Geo-monitoring PDF sync | `docs/GEO_MONITORING_SYNC.md` | Yes | DONE | Source PDF path, destination path, trigger, and verification. |
| Beacon GEO ad tool | `tools/create_beacon_geo_ads.py` | Yes | IMPLEMENTED | Generates Beacon GEO ad-style image outputs. |
| Tooling README | `tools/README.md` | Yes | DONE | Python, Pillow, run command, output directory, font notes. |
| Beacon GEO landing PRD | `beacon-geo-landing-prd.md` | Yes, force-added by DOC-REM | Implemented (homepage module + 3 blog posts inline) | Root PRD is normally ignored; committed for status alignment. |
| Beacon GEO homepage launch tech PRD | `beacon-geo-tech-prd.md` | No, gitignored | Ready for implementation (historical) | Superseded by the implemented landing page and site-update records. |
| Beacon GEO site update PRD | `beacon-geo-site-update-prd.md` | Yes, force-added by DOC-REM | Implemented - verified against index.html (2026-06-01) | Nav `#beacon-geo`, Keyword Map asset, and PDF CTA are shipped. |
| Beacon GEO site update tech PRD | `beacon-geo-site-update-tech-prd.md` | Yes, force-added by DOC-REM | Implemented - verified against index.html (2026-06-01) | Technical requirements match current `index.html`. |
| Module A design PRD | `module-a-design-prd.md` | Yes, force-added by DOC-REM | Finalized - Long Light palette (2026-05-22) | Header now matches finalized palette body text. |
| Module B content PRD | `module-b-content-prd.md` | Yes, force-added by DOC-REM | Partial - portfolio card URLs still placeholder (#) | Content model exists; portfolio URLs remain a known product gap. |
| Module C technical PRD | `module-c-technical-prd.md` | Yes, force-added by DOC-REM | Updated | Section 3 tree now includes Beacon GEO assets, `tools/`, `hero-illustration.png`, and `docs/`. |
| Blog 01 local source | `blog-01-what-does-ai-say-about-your-brand.md` | No, gitignored | IMPLEMENTED inline | Local source draft; public body must be synced manually into `index.html`. |
| Blog 02 local source | `blog-02-what-is-geo-and-how-can-a-company-measure-it.md` | No, gitignored | IMPLEMENTED inline | Displayed above Blog 01 on the homepage. |
| Blog 03 local source | `blog-03-beacon-geo-turning-ai-answers-into-a-brand-visibility-report.md` | No, gitignored | IMPLEMENTED inline | Displayed with Blog 02 above Blog 01. |

## Asset Hygiene Note

`case-folder/beacon-geo-report/beacon-geo-ad-01-prompt-strategy.png` was not deleted in DOC-REM because Step 0 found active references in `tools/create_beacon_geo_ads.py`. The public homepage uses `beacon-geo-ad-01-keyword-map.png`; the prompt-strategy PNG is kept as a tracked tool output/reference until the generator is intentionally refactored.
