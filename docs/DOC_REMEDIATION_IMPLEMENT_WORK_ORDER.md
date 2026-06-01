# UTAKATA HP — Documentation Remediation (DOC-REM)

> **Assign to:** Codex · **Kind:** `IMPLEMENT` · **Status:** `READY`  
> **Spec:** `docs/DOC_REMEDIATION_SPEC.md`  
> **Repo:** `UTAKATA HP` / `utakata-lab`  
> **Baseline:** `index.html` Beacon GEO module + 3 inline blogs already live; this WO is **docs + light hygiene only**

---

## Task summary

```text
Task: DOC-REM — Documentation remediation & publish ops
Owner: Codex
Kind: IMPLEMENT
```

**Product language:** Make the static-site repo maintainable — accurate README, tracked `docs/` playbooks, PRD status aligned with shipped homepage, remove dead asset if safe.

---

## Scope lock

| In scope | Out of scope |
|----------|--------------|
| Rewrite `README.md` per spec §6.1 | Visual redesign of homepage |
| Create `docs/INDEX.md`, `CONTENT_WORKFLOW.md`, `PUBLISH_CHECKLIST.md`, `GEO_MONITORING_SYNC.md` | Split `index.html` CSS/JS |
| Create `tools/README.md` | Portfolio `href="#"` → real URLs |
| Update PRD **Status** headers + Module C §3 tree + beacon site-update implementation record | geo-monitoring-app feature work |
| Delete `beacon-geo-ad-01-prompt-strategy.png` if zero references | Change `.gitignore` rules (unless PM asks) |
| Verify/add `og:image` only if `hero-illustration.png` or dedicated og asset used — document in checklist | New blog post content |

---

## Prerequisites (Codex — run first)

```powershell
cd "C:\Users\ywpan\OneDrive\文档\Claude\Projects\UTAKATA HP"
git status
git branch --show-current
```

Confirm workspace is UTAKATA HP, not `geo-monitoring-app`.

Verify sample PDF source (adjust path in docs if missing):

```powershell
Test-Path ".\case-folder\beacon-geo-report\beacon-geo-report-Sample-en.pdf"
```

Search before deleting old ad image:

```powershell
Select-String -Path ".\index.html",".\tools\*.py",".\docs\*.md",".\README.md" -Pattern "prompt-strategy" -SimpleMatch
```

---

## Implementation steps (ordered)

### Step 1 — Tracked operational docs

Create and fill (content per `DOC_REMEDIATION_SPEC.md` §6):

| File | Action |
|------|--------|
| `docs/INDEX.md` | CREATE |
| `docs/CONTENT_WORKFLOW.md` | CREATE |
| `docs/PUBLISH_CHECKLIST.md` | CREATE |
| `docs/GEO_MONITORING_SYNC.md` | CREATE |

Cross-link all four from `README.md`.

### Step 2 — README rewrite

Replace `README.md` with spec §6.1 content. Keep under ~120 lines. Include docs links and `npx serve -p 3000 .` preview command.

### Step 3 — tools/README.md

CREATE per spec §6.6.

### Step 4 — PRD status & tree (local files)

Edit headers and sections (do not rewrite full PRD bodies):

| File | Changes |
|------|---------|
| `beacon-geo-site-update-prd.md` | Status → Implemented; add § Implementation record (nav `#beacon-geo`, keyword-map png, PDF href) |
| `beacon-geo-site-update-tech-prd.md` | Status → Implemented |
| `beacon-geo-landing-prd.md` | Status → Implemented (module + 3 blogs) |
| `module-a-design-prd.md` | Status → Finalized; remove header "TBD by owner" |
| `module-b-content-prd.md` | Status → Partial (portfolio URLs `#`) |
| `module-c-technical-prd.md` | Replace §3 file tree; note index.html monolith >800 lines, split deferred; link `docs/PUBLISH_CHECKLIST.md` for og/favicon |

Mirror final status strings in `docs/INDEX.md` table.

### Step 5 — Asset hygiene

If Step 0 search shows **no** references to `beacon-geo-ad-01-prompt-strategy.png`:

```powershell
git rm "case-folder/beacon-geo-report/beacon-geo-ad-01-prompt-strategy.png"
```

If referenced, skip delete and note in `docs/INDEX.md`.

### Step 6 — og:image (optional, only if straightforward)

- If using `hero-illustration.png` for OG: add `<meta property="og:image" content="...">` with **absolute** URL suitable for GitHub Pages (document assumption in `PUBLISH_CHECKLIST.md`).
- If no stable public base URL: **do not** add broken relative og:image; checklist item stays unchecked with note "pending asset".

### Step 7 — Git commit (tracked files only)

Stage tracked deliverables:

```text
README.md
docs/INDEX.md
docs/CONTENT_WORKFLOW.md
docs/PUBLISH_CHECKLIST.md
docs/GEO_MONITORING_SYNC.md
docs/DOC_REMEDIATION_SPEC.md
docs/DOC_REMEDIATION_IMPLEMENT_WORK_ORDER.md
tools/README.md
index.html                    (only if Step 6 changed)
case-folder/...               (only if Step 5 rm)
```

**Optional** (PM approval): force-add updated PRDs:

```powershell
git add -f beacon-geo-site-update-prd.md beacon-geo-site-update-tech-prd.md beacon-geo-landing-prd.md module-a-design-prd.md module-b-content-prd.md module-c-technical-prd.md
```

Suggested commit message:

```text
docs: add publish ops playbooks and align README with repo layout

- Add docs/ for content workflow, publish checklist, geo-monitoring PDF sync
- Rewrite README with preview and tracked vs local file guidance
- Mark Beacon site-update PRDs implemented; refresh module-c file tree
- Remove unused prompt-strategy ad asset (if unreferenced)
```

Do **not** push unless PM requests.

---

## Acceptance criteria

### Documentation

- [ ] **REM-1** `README.md` lists publishable vs local-only files and links all new `docs/*.md` files.
- [ ] **REM-2** `docs/CONTENT_WORKFLOW.md` states blog md → index.html sync and display order vs file numbering.
- [ ] **REM-3** `docs/PUBLISH_CHECKLIST.md` includes PDF CTA, bilingual toggle, img 404, og:image, mobile nav checks.
- [ ] **REM-4** `docs/GEO_MONITORING_SYNC.md` documents source path in geo-monitoring-app and dest path in HP repo.
- [ ] **REM-5** `docs/INDEX.md` inventories PRDs with statuses matching §6.7 (no Draft on shipped Beacon nav/Keyword Map/PDF).
- [ ] **REM-6** `module-c-technical-prd.md` §3 tree includes `beacon-geo-report/`, `tools/`, `hero-illustration.png`, `docs/`.
- [ ] **REM-7** `tools/README.md` documents Python, Pillow, run command, output directory.

### PRD alignment

- [ ] **REM-8** `beacon-geo-site-update-prd.md` and tech variant headers say **Implemented**.
- [ ] **REM-9** `beacon-geo-landing-prd.md` header reflects homepage + 3 inline blogs shipped.
- [ ] **REM-10** `module-a-design-prd.md` header says **Finalized** (Long Light), not TBD.

### Hygiene

- [ ] **REM-11** `beacon-geo-ad-01-prompt-strategy.png` removed OR documented why kept in `docs/INDEX.md`.
- [ ] **REM-12** No broken internal links in new md files (relative paths valid from repo root).

### Manual smoke (Codex)

- [ ] **REM-13** `npx serve -p 3000 .` → open `/` → Beacon carousel, PDF button, EN/JP toggle work.
- [ ] **REM-14** Click **Download Example Report** → PDF loads (not 404).

---

## Deliverables checklist

| Deliverable | Path |
|-------------|------|
| Spec (this initiative) | `docs/DOC_REMEDIATION_SPEC.md` |
| Work order | `docs/DOC_REMEDIATION_IMPLEMENT_WORK_ORDER.md` |
| Doc index | `docs/INDEX.md` |
| Content workflow | `docs/CONTENT_WORKFLOW.md` |
| Publish checklist | `docs/PUBLISH_CHECKLIST.md` |
| PDF sync | `docs/GEO_MONITORING_SYNC.md` |
| Entry readme | `README.md` |
| Tooling readme | `tools/README.md` |

---

## Codex handoff prompt (copy-paste)

```text
Implement UTAKATA HP task DOC-REM per:
- docs/DOC_REMEDIATION_SPEC.md
- docs/DOC_REMEDIATION_IMPLEMENT_WORK_ORDER.md

Repo: C:\Users\ywpan\OneDrive\文档\Claude\Projects\UTAKATA HP

Follow WO steps 0–7 in order. Satisfy acceptance criteria REM-1 through REM-14.
Scope: documentation and light static hygiene only; no homepage redesign.
Commit tracked files with suggested message; do not push.
Report: files changed, REM checklist, PDF source Test-Path result, whether prompt-strategy png was deleted.
```

---

## PM notes after Codex completes

1. Review `docs/PUBLISH_CHECKLIST.md` on next real deploy.
2. Decide whether to `git add -f` root PRDs for GitHub visibility.
3. If og:image still pending, supply `docs/assets/og-image.png` or reuse cropped hero in follow-up WO.
