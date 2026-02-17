from pathlib import Path
import random

from PIL import Image, ImageDraw, ImageFont

_FONT_CANDIDATES = (
    "arial.ttf",
    "DejaVuSans.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
)


def _load_font(size=40):
    for font_path in _FONT_CANDIDATES:
        try:
            return ImageFont.truetype(font_path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def create_meme(topic):
    img = Image.open("static/template.jpg")
    draw = ImageDraw.Draw(img)

    safe_topic = (topic or "this").strip() or "this"
    caption = f"When you think about {safe_topic} too much..."
    font = _load_font(40)

    draw.text((10, 10), caption, font=font, fill="white")

    output_path = Path("static") / f"meme_{random.randint(1, 10000)}.jpg"
    img.save(output_path)
    return str(output_path)
