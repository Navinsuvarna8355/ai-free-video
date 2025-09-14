import os
from PIL import Image, ImageDraw, ImageFont

def generate_images(scenes):
    os.makedirs("assets/images", exist_ok=True)
    for i, scene in enumerate(scenes):
        img = Image.new("RGB", (720, 480), color="white")
        draw = ImageDraw.Draw(img)
        draw.text((50, 200), scene[:100], fill="black")
        img.save(f"assets/images/scene_{i}.png")
