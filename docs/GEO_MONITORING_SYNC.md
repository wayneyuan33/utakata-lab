# Geo-monitoring PDF Sync

## EN - Sync Contract

| Item | Value |
|---|---|
| Source repo | `C:\dev\geo-monitoring-app` |
| Source file | `outputs/GEO_Monitoring_Report_Sample_Anonymized.pdf` |
| Dest in HP repo | `case-folder/beacon-geo-report/beacon-geo-example-report.pdf` |
| Trigger | New anonymized sample after a Beacon GEO product release |
| Verification | Open the homepage Beacon GEO secondary CTA in a new tab and confirm the PDF loads |

Step 0 on 2026-06-01 returned `False` for the source file path and `True` for the HP destination PDF. If the product repo moves the sample, update both this file and the product repo docs before copying.

## JP - 同期メモ

新しい匿名化サンプル PDF が出たら、`geo-monitoring-app` からこの HP リポジトリの Beacon GEO CTA 用 PDF にコピーします。

## Copy Steps

From the HP repo root:

```powershell
$source = "C:\dev\geo-monitoring-app\outputs\GEO_Monitoring_Report_Sample_Anonymized.pdf"
$dest = ".\case-folder\beacon-geo-report\beacon-geo-example-report.pdf"
Test-Path $source
Test-Path $dest
Copy-Item -LiteralPath $source -Destination $dest -Force
```

Only run `Copy-Item` when the source path exists and the sample is approved for public anonymized distribution.

## Verification

1. Run `npx serve -p 3000 .` from this repo.
2. Open `http://localhost:3000/`.
3. Click `Download Example Report` in the Beacon GEO section.
4. Confirm the new tab loads the PDF and is not a 404.
5. Commit the PDF only when the content has been approved.
