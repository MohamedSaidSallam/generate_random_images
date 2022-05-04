import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

COLORS = [(249, 255, 255),  # f9ffff White
          (156, 157, 151),  # 9c9d97 Light gray
          (71, 79, 82),  # 474f52 Gray
          (29, 28, 33),  # 1d1c21 Black
          (255, 216, 61),  # ffd83d Yellow
          (249, 128, 29),  # f9801d Orange
          (176, 46, 38),  # b02e26 Red
          (130, 84, 50),  # 825432 Brown
          (128, 199, 31),  # 80c71f Lime
          (93, 124, 21),  # 5d7c15 Green
          (58, 179, 218),  # 3ab3da Light Blue
          (22, 156, 157),  # 169c9d Cyan
          (60, 68, 169),  # 3c44a9 blue
          (243, 140, 170),  # f38caa Pink
          (198, 79, 189),  # c64fbd Magenta
          (137, 50, 183)  # 8932b7 Purple
          ]

IMAGE_SIZE = 400
FONT_SIZE = 80
FONT_FILE = "Roboto-Regular.ttf"

NUM_COLORS = 10
RECTANGLE_INCREMENT = IMAGE_SIZE / NUM_COLORS

NUM_IMAGES = 1000
OUTPUT_FOLDER = 'output'
Path(OUTPUT_FOLDER).mkdir(parents=True, exist_ok=True)

font = ImageFont.truetype(FONT_FILE, FONT_SIZE)
history = {}
for index in range(NUM_IMAGES):
    img = Image.new("RGB", (IMAGE_SIZE, IMAGE_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw.text((0, IMAGE_SIZE - FONT_SIZE), f"#{index}", (0, 0, 0), font=font)

    while True:
        colorsInOrder = random.choices(COLORS, k=NUM_COLORS)
        if str(colorsInOrder) not in history:
            history[str(colorsInOrder)] = True
            for i in range(NUM_COLORS):
                draw.rectangle((i * RECTANGLE_INCREMENT, 0, (i+1) *
                                RECTANGLE_INCREMENT, (i+1) * RECTANGLE_INCREMENT), fill=colorsInOrder[i])
            break

    img.save(f"{OUTPUT_FOLDER}/{index}.png")
