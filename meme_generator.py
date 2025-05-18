from PIL import Image, ImageDraw, ImageFont
import random

def create_meme(topic):
    img = Image.open("static/template.jpg")
    draw = ImageDraw.Draw(img)
    caption = f"When you think about {topic} too much..."
    font = ImageFont.truetype("arial.ttf", 40)
    draw.text((10, 10), caption, font=font, fill="white")
    output_path = f"static/meme_{random.randint(1, 10000)}.jpg"
    img.save(output_path)
    return output_path