from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "case-folder" / "beacon-geo-report"
SOURCE_PANELS = OUT / "source-panels"
SOURCE_PANELS.mkdir(parents=True, exist_ok=True)

W, H = 1600, 1000

COLORS = {
    "deep": "#1B1F1E",
    "dark": "#4A524A",
    "mid": "#7D8278",
    "light": "#D8D6CE",
    "cream": "#F2EEE6",
    "accent": "#C47A3A",
    "accent_hover": "#A8612A",
    "accent_light": "#E7C5B6",
}

FONT_DIR = Path(r"C:\Windows\Fonts")
FONT_BOLD = FONT_DIR / "arialbd.ttf"
FONT_REG = FONT_DIR / "arial.ttf"


def font(path, size):
    return ImageFont.truetype(str(path), size)


F = {
    "brand": font(FONT_BOLD, 25),
    "label": font(FONT_REG, 20),
    "num": font(FONT_BOLD, 116),
    "title": font(FONT_BOLD, 78),
    "subtitle": font(FONT_REG, 34),
    "meta": font(FONT_REG, 24),
}


def rgba(hex_color, alpha=255):
    h = hex_color.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (alpha,)


def rounded_mask(size, radius):
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=255)
    return mask


def fit_contain(im, size, fill="#101514"):
    src_w, src_h = im.size
    dst_w, dst_h = size
    scale = min(dst_w / src_w, dst_h / src_h)
    resized = im.resize((round(src_w * scale), round(src_h * scale)), Image.LANCZOS)
    canvas = Image.new("RGBA", size, rgba(fill, 255))
    left = (dst_w - resized.width) // 2
    top = (dst_h - resized.height) // 2
    canvas.alpha_composite(resized, (left, top))
    return canvas


def add_shadow(base, layer, xy, blur=44, offset=(0, 28), alpha=115):
    shadow = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    shadow.putalpha(layer.split()[-1].point(lambda p: int(p * alpha / 255)))
    shadow = shadow.filter(ImageFilter.GaussianBlur(blur))
    base.alpha_composite(shadow, (xy[0] + offset[0], xy[1] + offset[1]))
    base.alpha_composite(layer, xy)


def draw_wrapped(draw, text, xy, font_obj, fill, max_width, line_gap=9):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=font_obj)[2] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)

    y = xy[1]
    for line in lines:
        draw.text((xy[0], y), line, font=font_obj, fill=fill)
        bbox = draw.textbbox((xy[0], y), line, font=font_obj)
        y += (bbox[3] - bbox[1]) + line_gap
    return y


def draw_background(base, bg, accent):
    draw = ImageDraw.Draw(base)
    base.alpha_composite(Image.new("RGBA", base.size, rgba(bg, 255)))

    draw.rectangle((0, 0, 30, H), fill=rgba(accent, 255))
    draw.rectangle((30, 0, 54, H), fill=rgba(COLORS["accent_light"], 160))
    draw.rounded_rectangle((1090, 92, 1548, 908), radius=48, fill=rgba(COLORS["cream"], 18))
    draw.rounded_rectangle((642, 170, 1528, 870), radius=54, outline=rgba(COLORS["accent_light"], 95), width=2)


def draw_brand(draw):
    draw.text((112, 86), "BEACON GEO", font=F["brand"], fill=COLORS["cream"])
    draw.text((112, 122), "AI VISIBILITY", font=F["label"], fill=rgba(COLORS["cream"], 155))
    draw.rounded_rectangle((1316, 78, 1508, 124), radius=23, outline=rgba(COLORS["cream"], 85), width=2)
    draw.text((1342, 89), "UTAKATA LAB", font=F["label"], fill=rgba(COLORS["cream"], 200))


def draw_copy(draw, spec):
    accent = spec["accent"]
    x = 112
    draw.text((x, 214), f"0{spec['num']}", font=F["num"], fill=accent)
    y = 356
    for line in spec["title"]:
        draw.text((x, y), line, font=F["title"], fill=COLORS["cream"])
        y += 88
    draw_wrapped(draw, spec["subtitle"], (x, y + 26), F["subtitle"], rgba(COLORS["cream"], 210), 470)
    draw.line((x, 836, x + 330, 836), fill=accent, width=5)
    draw.text((x, 866), spec["kicker"], font=F["meta"], fill=rgba(COLORS["cream"], 175))


def make_panel(panel_path, size, crop_box=None):
    panel = Image.open(panel_path).convert("RGBA")
    if crop_box:
        panel = panel.crop(crop_box)
    panel = ImageEnhance.Color(panel).enhance(0.52)
    panel = ImageEnhance.Contrast(panel).enhance(0.96)
    panel = fit_contain(panel, size)
    panel = panel.filter(ImageFilter.UnsharpMask(radius=1.2, percent=105, threshold=4))

    shell = Image.new("RGBA", (size[0] + 38, size[1] + 70), (0, 0, 0, 0))
    draw = ImageDraw.Draw(shell)
    draw.rounded_rectangle((0, 0, shell.width - 1, shell.height - 1), radius=34,
                           fill=rgba("#101514", 245), outline=rgba(COLORS["cream"], 90), width=2)
    draw.ellipse((24, 22, 38, 36), fill=rgba(COLORS["accent"], 245))
    draw.ellipse((48, 22, 62, 36), fill=rgba(COLORS["accent_light"], 230))
    draw.ellipse((72, 22, 86, 36), fill=rgba(COLORS["mid"], 230))
    shell.alpha_composite(panel, (19, 52))
    shell.putalpha(rounded_mask(shell.size, 34))
    return shell


def prepare_source_panels():
    crops = [
        {
            "file": "beacon-geo-ad-01-prompt-strategy.png",
            "box": (790, 152, 1600, 998),
            "out": "beacon-geo-ui-01.png",
        },
        {
            "file": "beacon-geo-ad-02-ai-answer-capture.png",
            "box": (664, 250, 1576, 606),
            "out": "beacon-geo-ui-02.png",
        },
        {
            "file": "beacon-geo-ad-03-visibility-metrics.png",
            "box": (776, 232, 1582, 880),
            "out": "beacon-geo-ui-03.png",
        },
        {
            "file": "beacon-geo-ad-04-report-output.png",
            "box": (748, 156, 1590, 934),
            "out": "beacon-geo-ui-04.png",
        },
    ]

    for item in crops:
        target = SOURCE_PANELS / item["out"]
        if target.exists():
            continue
        source = Image.open(OUT / item["file"]).convert("RGBA")
        source.crop(item["box"]).save(target)


SLIDES = [
    {
        "num": 1,
        "title": ["PROMPT", "MAP"],
        "subtitle": "Build the questions AI will answer.",
        "kicker": "Strategy setup",
        "panel": "beacon-geo-ui-01.png",
        "panel_crop": (34, 40, 798, 832),
        "panel_size": (820, 620),
        "panel_xy": (640, 212),
        "bg": "#3F4841",
        "accent": COLORS["accent"],
        "out": "beacon-geo-ad-01-prompt-strategy.png",
    },
    {
        "num": 2,
        "title": ["ANSWER", "RUN"],
        "subtitle": "Capture model responses at scale.",
        "kicker": "Live collection",
        "panel": "beacon-geo-ui-02.png",
        "panel_crop": (34, 40, 890, 314),
        "panel_size": (835, 365),
        "panel_xy": (655, 304),
        "bg": "#343D38",
        "accent": COLORS["accent_light"],
        "out": "beacon-geo-ad-02-ai-answer-capture.png",
    },
    {
        "num": 3,
        "title": ["VISIBILITY", "LENS"],
        "subtitle": "See who AI recommends.",
        "kicker": "Coverage and share of voice",
        "panel": "beacon-geo-ui-03.png",
        "panel_crop": (48, 52, 782, 628),
        "panel_size": (830, 565),
        "panel_xy": (650, 238),
        "bg": COLORS["deep"],
        "accent": COLORS["accent"],
        "out": "beacon-geo-ad-03-visibility-metrics.png",
    },
    {
        "num": 4,
        "title": ["REPORT", "VIEW"],
        "subtitle": "Turn evidence into action.",
        "kicker": "Executive-ready output",
        "panel": "beacon-geo-ui-04.png",
        "panel_crop": (48, 52, 812, 750),
        "panel_size": (825, 610),
        "panel_xy": (648, 218),
        "bg": COLORS["dark"],
        "accent": COLORS["accent_light"],
        "out": "beacon-geo-ad-04-report-output.png",
    },
]


def make_slide(spec):
    base = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_background(base, spec["bg"], spec["accent"])
    draw = ImageDraw.Draw(base)
    draw_brand(draw)
    draw_copy(draw, spec)

    panel = make_panel(SOURCE_PANELS / spec["panel"], spec["panel_size"], spec.get("panel_crop"))
    add_shadow(base, panel, spec["panel_xy"])

    final = base.convert("RGB")
    path = OUT / spec["out"]
    final.save(path, quality=96, optimize=True)
    return path


if __name__ == "__main__":
    prepare_source_panels()
    outputs = [make_slide(spec) for spec in SLIDES]
    for output in outputs:
        print(output)
