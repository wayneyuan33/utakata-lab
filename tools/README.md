# Beacon GEO Asset Tooling

`create_beacon_geo_ads.py` generates ad-style Beacon GEO visual assets used by the homepage carousel.

## Requirements

- Python 3
- Pillow

Install Pillow locally:

```powershell
pip install pillow
```

## Run

From the repo root:

```powershell
python tools/create_beacon_geo_ads.py
```

## Outputs

Generated images are written under:

`case-folder/beacon-geo-report/`

Current homepage carousel assets include:

- `beacon-geo-ad-01-keyword-map.png`
- `beacon-geo-ad-02-ai-answer-capture.png`
- `beacon-geo-ad-03-visibility-metrics.png`
- `beacon-geo-ad-04-report-output.png`

## Font Notes

The script includes Windows font path assumptions. On non-Windows systems, edit the font path lookup before regenerating assets so text rendering remains stable.
