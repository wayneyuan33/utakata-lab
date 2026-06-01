# Geo-monitoring PDF Sync

## EN - Sync Contract

| Item | Value |
|---|---|
| Source repo | `UTAKATA HP` |
| Source file | `case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf` |
| Dest in HP repo | `case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf` |
| Trigger | New anonymized sample after a Beacon GEO product release |
| Verification | Open the homepage Beacon GEO secondary CTA in a new tab and confirm the PDF loads |

2026-06-01 update: the homepage CTA uses `case-folder/beacon-geo-report/beacon-geo-report-Sample-en.pdf`; the old geo-monitoring output path is no longer used.

## JP - 同期メモ

新しい匿名化サンプル PDF が出たら、`geo-monitoring-app` からこの HP リポジトリの Beacon GEO CTA 用 PDF にコピーします。

## Copy Steps

From the HP repo root:

```powershell
$pdf = ".\case-folder\beacon-geo-report\beacon-geo-report-Sample-en.pdf"
Test-Path $pdf
```

Only replace this PDF when the sample is approved for public anonymized distribution.

## Verification

1. Run `npx serve -p 3000 .` from this repo.
2. Open `http://localhost:3000/`.
3. Click `Download Example Report` in the Beacon GEO section.
4. Confirm the new tab loads the PDF and is not a 404.
5. Commit the PDF only when the content has been approved.
