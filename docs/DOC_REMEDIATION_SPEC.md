# UTAKATA HP — Documentation Remediation Spec

> **Version:** 1.0  
> **Date:** 2026-06-01  
> **Status:** Approved for implementation  
> **Owner:** UTAKATA LAB / PM  
> **Assignee:** Codex  
> **Related WO:** `docs/DOC_REMEDIATION_IMPLEMENT_WORK_ORDER.md`  
> **Trigger:** Documentation health review (2026-06-01) — README thin, PRD status stale, file tree drift, no publish/sync workflow.

---

## 1. Background

The UTAKATA HP repo (`utakata-lab`) is a **zero-build static site**: `index.html` + `case-folder/` assets. Product work (Beacon GEO module, blogs, nav) is largely **implemented**, but **documentation lags code**:

| Gap | Risk |
|-----|------|
| `README.md` does not explain local vs publishable files, preview, or PDF sync from `geo-monitoring-app` | New contributors break publish or ship stale sample PDF |
| Root `*-prd.md` files still say Draft while `index.html` is live | Duplicate or abandoned implementation work |
| `module-c-technical-prd.md` file tree omits `beacon-geo-report/`, `tools/`, root `hero-illustration.png` | Wrong mental model for asset paths |
| Blog copy exists in **two places**: gitignored `blog-*.md` and tracked `index.html` | Edits to md only do not update the site |
| No publish checklist | og:image, favicon, 404 on PDF left untracked |
| Unused asset `beacon-geo-ad-01-prompt-strategy.png` still in repo | Confusion + repo bloat |

This spec defines **documentation and light static-site hygiene** only. No redesign, no new sections, no CMS.

---

## 2. Goals

### 2.1 Business goal

Make the repo **self-explanatory for Codex, future-you, and PM** within one read of `README.md` + `docs/`, so handoffs do not depend on chat history.

### 2.2 Documentation goals

1. **Single entry:** `README.md` links to all operational docs under `docs/`.
2. **Truthful PRD status:** Implemented Beacon site-update PRDs marked done; Module A palette status aligned with body text.
3. **Accurate architecture tree:** Module C §3 matches repository layout (2026-06).
4. **Explicit workflows:** Content edit path (blog md → index), PDF sample sync from geo-monitoring-app, local preview, publish checklist.
5. **Tracked ops docs:** New files under `docs/` are **git-tracked** (not matched by `*-prd.md` ignore rule).

### 2.3 Optional code hygiene (in scope)

- Remove unused tracked image `case-folder/beacon-geo-report/beacon-geo-ad-01-prompt-strategy.png` if no references remain.
- Add `og:image` meta when `docs/assets/og-image.png` exists OR document placeholder path in checklist until asset is supplied.

---

## 3. Non-goals

| Out of scope | Reason |
|--------------|--------|
| Splitting `index.html` into CSS/JS files | Separate refactor; file size noted in Module C only |
| Portfolio card real URLs (`href="#"` → live demos) | Product decision; document as known gap |
| Translating all PRDs to Chinese | English PRDs stay; new ops docs bilingual per §5 |
| Changing `.gitignore` to track all root `*-prd.md` | Optional follow-up; WO uses `git add -f` for PRD status-only edits if PM wants them on remote |
| geo-monitoring-app code changes | PDF **copy** only, from existing sample path |

---

## 4. Target information architecture

```text
README.md                          ← Entry: what ships, how to preview, link to docs/
docs/
  INDEX.md                         ← Doc map + PRD inventory + status
  CONTENT_WORKFLOW.md              ← blog-*.md ↔ index.html, bilingual QA
  PUBLISH_CHECKLIST.md             ← Pre-flight before GitHub Pages / Vercel
  GEO_MONITORING_SYNC.md           ← PDF + sample report path from sibling repo
  DOC_REMEDIATION_SPEC.md          ← This file
  DOC_REMEDIATION_IMPLEMENT_WORK_ORDER.md
tools/
  README.md                        ← create_beacon_geo_ads.py usage
```

Root planning PRDs (`module-*.md`, `beacon-geo-*.md`, `blog-*.md`) **remain gitignored** unless PM runs `git add -f`; WO still requires **status header updates** on disk for local consistency.

---

## 5. Language policy for new docs

| Audience | Language |
|----------|----------|
| `README.md` | English primary; short 日本語/中文 pointer line optional in footer |
| `docs/CONTENT_WORKFLOW.md`, `docs/PUBLISH_CHECKLIST.md`, `docs/GEO_MONITORING_SYNC.md` | **Bilingual section headers** (EN block, then JP or ZH one-liner where critical) — keep procedural steps in English for Codex parity with PRDs |
| `docs/INDEX.md` | English table; status column uses `DONE` / `DRAFT` / `IMPLEMENTED` |

---

## 6. Content requirements (by file)

### 6.1 `README.md` (rewrite, ≤120 lines)

Must include:

1. Project one-liner + link to live site if known (`https://wayneyuan33.github.io/utakata-lab/` or placeholder).
2. **What gets published** (tracked paths only).
3. **What stays local** (gitignored patterns: `*-prd.md`, `blog-*.md`, collateral list from `.gitignore` — summarized, not full dump).
4. **Local preview:** `npx serve -p 3000 .` (align with `.claude/launch.json`).
5. **Directory tree** (abbreviated, accurate — include `beacon-geo-report/`, `tools/`).
6. Links to `docs/INDEX.md`, `CONTENT_WORKFLOW.md`, `PUBLISH_CHECKLIST.md`, `GEO_MONITORING_SYNC.md`.
7. **Related repo:** `geo-monitoring-app` (Beacon GEO product); one sentence on relationship.

### 6.2 `docs/INDEX.md`

Table columns: Document | Path | Git tracked? | Status | Notes

Minimum rows:

- All `module-*.md`, `beacon-geo-*.md`, `blog-*.md` (with corrected status)
- New docs from this spec
- `index.html`, `tools/create_beacon_geo_ads.py`

### 6.3 `docs/CONTENT_WORKFLOW.md`

Must document:

1. **Source of truth for blog body:** `blog-NN-*.md` → manual sync into `<article class="blog-post">` in `index.html`.
2. **Display order vs file numbering:** Page shows newest first (02, 03 on top; 01 oldest at bottom).
3. **Bilingual:** Every post needs `data-en` / `data-jp` blocks; language toggle QA steps.
4. **Adding post #4:** Copy template comment in `index.html` + add matching `blog-04-*.md` locally.
5. **Do not** edit only md and expect deploy to update.

### 6.4 `docs/PUBLISH_CHECKLIST.md`

Checkbox list including:

- [ ] `index.html` opens locally without console errors
- [ ] All `img` / `a href` under `case-folder/` resolve (no 404)
- [ ] `case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf` opens from CTA
- [ ] EN/JP toggle on nav, Beacon, blogs, contact
- [ ] `og:title`, `og:description`; `og:image` if file present
- [ ] Mobile nav at 768px / 1024px (Beacon nav item not broken)
- [ ] Remove or avoid committing gitignored collateral
- [ ] After PDF update: run sync steps in `GEO_MONITORING_SYNC.md`

### 6.5 `docs/GEO_MONITORING_SYNC.md`

Must document:

| Item | Value |
|------|--------|
| Source repo | `C:\dev\geo-monitoring-app` (or clone path) |
| Source file | `case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf` (verify path exists; if moved, update both repos' docs) |
| Dest in HP repo | `case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf` |
| Trigger | New anonymized sample after product release |
| Verification | Open secondary CTA on homepage in new tab |

### 6.6 `tools/README.md`

- Python 3 + `pip install pillow`
- Run: `python tools/create_beacon_geo_ads.py` from repo root
- Outputs under `case-folder/beacon-geo-report/`
- Windows font paths note; non-Windows may need font path edit

### 6.7 PRD status updates (on-disk, headers only)

| File | New status line |
|------|-----------------|
| `beacon-geo-site-update-prd.md` | `**Status:** Implemented — verified against index.html (2026-06-01)` |
| `beacon-geo-site-update-tech-prd.md` | Same |
| `beacon-geo-landing-prd.md` | `**Status:** Implemented (homepage module + 3 blog posts inline)` |
| `module-a-design-prd.md` | `**Status:** Finalized — Long Light palette (2026-05-22)` — remove "TBD by owner" from header |
| `module-b-content-prd.md` | `**Status:** Partial — portfolio card URLs still placeholder (#)` |
| `module-c-technical-prd.md` | Replace §3 file tree; add note: single-file `index.html` >800 lines, split deferred |

Add § **Implementation record** at bottom of `beacon-geo-site-update-prd.md` (3 bullets): nav, Keyword Map asset, PDF CTA — each with `index.html` anchor ids/paths.

### 6.8 `module-c-technical-prd.md` §3 tree (accurate)

```text
/
├── index.html
├── hero-illustration.png
├── README.md
├── tools/
│   ├── README.md
│   └── create_beacon_geo_ads.py
├── case-folder/
│   ├── beacon-geo-report/
│   │   ├── beacon-geo-report-Sample-en.pdf
│   │   ├── beacon-geo-ad-01-keyword-map.png
│   │   ├── beacon-geo-ad-02-ai-answer-capture.png
│   │   ├── beacon-geo-ad-03-visibility-metrics.png
│   │   ├── beacon-geo-ad-04-report-output.png
│   │   └── source-panels/
│   ├── luxury-beauty-llmo-case/
│   └── top-10-tech-trend-personality-test/
└── docs/                    ← tracked operational docs
```

Remove or mark `/assets/` as **FUTURE** with checklist link to `PUBLISH_CHECKLIST.md`.

---

## 7. Acceptance criteria (spec level)

- [ ] **DR-1** A new contributor can preview the site and find PDF sync steps without reading chat logs.
- [ ] **DR-2** `docs/INDEX.md` PRD status matches implementation reality for Beacon site-update and landing PRDs.
- [ ] **DR-3** No document claims "Draft" for shipped Beacon nav/Keyword Map/PDF features.
- [ ] **DR-4** Blog workflow explicitly warns against md-only edits.
- [ ] **DR-5** Publish checklist covers PDF, bilingual, and og:image gap.
- [ ] **DR-6** Unused `beacon-geo-ad-01-prompt-strategy.png` removed from repo if unreferenced.

---

## 8. Risks

| Risk | Mitigation |
|------|------------|
| PRD edits gitignored → not on GitHub | WO lists `git add -f` optional step; tracked `docs/INDEX.md` mirrors status |
| Sample PDF path missing in geo-monitoring-app | WO: verify path; if absent, note in SYNC doc and skip copy |
| og:image asset missing | Checklist item "blocked"; do not invent URL |

---

## 9. References

- Prior review: Cursor documentation health check (2026-06-01)
- Product PRDs: `beacon-geo-landing-prd.md`, `beacon-geo-site-update-prd.md`
- Architecture: `module-c-technical-prd.md` v1.1
- Remote: `https://github.com/wayneyuan33/utakata-lab.git`
