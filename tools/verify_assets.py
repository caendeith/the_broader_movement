import os
from PIL import Image

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets"))
VIOLET = (138, 43, 226)
PINK = (255, 77, 141)
GOLD = (255, 194, 75)
WHITE = (246, 242, 255)


def near(c, t, tol=26):
    return all(abs(a - b) <= tol for a, b in zip(c[:3], t[:3]))


for f in ["logo.png", "banner.png", "og-image.png", "icon-512.png", "favicon-64.png"]:
    p = os.path.join(OUT, f)
    im = Image.open(p).convert("RGBA")
    w, h = im.size
    px = im.load()
    counts = {"violet": 0, "pink": 0, "gold": 0, "white": 0}
    transparent = 0
    step = 1 if w * h < 400000 else 4
    for y in range(0, h, step):
        for x in range(0, w, step):
            r, g, b, a = px[x, y]
            if a < 40:
                transparent += 1
                continue
            if near((r, g, b), VIOLET):
                counts["violet"] += 1
            elif near((r, g, b), PINK):
                counts["pink"] += 1
            elif near((r, g, b), GOLD):
                counts["gold"] += 1
            elif near((r, g, b), WHITE):
                counts["white"] += 1
    total = ((w // step) + 1) * ((h // step) + 1)
    print(f"{f:14s} {im.size}  transparent={transparent/total:.3f}  {counts}")
