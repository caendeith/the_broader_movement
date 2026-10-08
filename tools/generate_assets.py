import math, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(BASE, "..", "assets"))
os.makedirs(OUT, exist_ok=True)

FONTS = r"C:\Windows\Fonts"
BOLD = os.path.join(FONTS, "segoeuib.ttf")
SEMI = os.path.join(FONTS, "seguisb.ttf")
REG = os.path.join(FONTS, "segoeui.ttf")
MONO = os.path.join(FONTS, "consolab.ttf")

# Brand palette (RGBA)
VIOLET = (138, 43, 226, 255)   # #8A2BE2  — Bro / brotherhood
PINK   = (255, 77, 141, 255)   # #FF4D8D  — Broad / warmth & access
GOLD   = (255, 194, 75, 255)   # #FFC24B  — Pay it forward
CYAN   = (77, 225, 255, 255)   # #4DE1FF  — tech accent
WHITE  = (246, 242, 255, 255)
MUTED  = (172, 162, 210, 255)
BG_TOP = (32, 21, 70)
BG_BOT = (9, 5, 22)


def vgrad(size, top, bot):
    w, h = size
    t = np.linspace(0.0, 1.0, h)[:, None].astype(np.float32)
    arr = np.round(
        np.array(top, dtype=np.float32) * (1 - t) + np.array(bot, dtype=np.float32) * t
    ).astype(np.uint8)
    arr = np.repeat(arr[:, None, :], w, axis=1)  # (h, w, 3)
    return Image.fromarray(arr, "RGB").convert("RGBA")


def pt(cx, cy, deg, r):
    a = math.radians(deg)
    return (cx + r * math.cos(a), cy + r * math.sin(a))


def draw_mark(d, cx, cy, R, W):
    """The Broader Loop: 3 colored arcs (3 Laws) with a flowing arrowhead."""
    segs = [(0, 100, VIOLET), (120, 100, PINK), (240, 100, GOLD)]
    for start, span, color in segs:
        end = start + span
        d.arc([cx - R, cy - R, cx + R, cy + R], start, end, fill=color, width=W)
        # rounded cap at the start
        x, y = pt(cx, cy, start, R)
        rr = W / 2.0
        d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=color)
        # arrowhead at the clockwise end
        e = math.radians(end)
        Tx, Ty = -math.sin(e), math.cos(e)  # clockwise tangent
        Nx, Ny = math.cos(e), math.sin(e)   # outward normal
        bx, by = pt(cx, cy, end, R)
        L = W * 1.05
        hw = W * 0.72
        tip = (bx + Tx * L, by + Ty * L)
        b1 = (bx + Nx * hw, by + Ny * hw)
        b2 = (bx - Nx * hw, by - Ny * hw)
        d.polygon([tip, b1, b2], fill=color)


def draw_monogram(img, cx, cy, size, glow_color=(150, 90, 255, 170)):
    """Bold 'B' with a soft glow, centered on (cx, cy)."""
    font = ImageFont.truetype(BOLD, size)
    tmp = ImageDraw.Draw(img)
    b = tmp.textbbox((0, 0), "B", font=font)
    tw, th = b[2] - b[0], b[3] - b[1]
    tx = cx - (b[0] + tw / 2.0)
    ty = cy - (b[1] + th / 2.0)
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.text((tx, ty), "B", font=font, fill=glow_color)
    glow = glow.filter(ImageFilter.GaussianBlur(max(4, size * 0.06)))
    img = Image.alpha_composite(img, glow)
    d = ImageDraw.Draw(img)
    d.text((tx, ty), "B", font=font, fill=WHITE)
    return img


def rounded_mask(size, radius):
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, size[0] - 1, size[1] - 1], radius=radius, fill=255)
    return m


def make_logo(size=1024, radius=210):
    S = size * 2  # supersample
    img = vgrad((S, S), BG_TOP, BG_BOT)
    # ambient glow behind the loop
    glow = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([S * 0.16, S * 0.16, S * 0.84, S * 0.84], fill=(120, 60, 220, 70))
    glow = glow.filter(ImageFilter.GaussianBlur(S * 0.05))
    img = Image.alpha_composite(img, glow)
    d = ImageDraw.Draw(img)
    cx = cy = S // 2
    draw_mark(d, cx, cy, int(S * 0.30), int(S * 0.050))
    img = draw_monogram(img, cx, cy, int(S * 0.40))
    img = img.resize((size, size), Image.LANCZOS)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0), rounded_mask((size, size), radius))
    return out


def make_icon(size=512, radius=110):
    S = size * 2
    img = vgrad((S, S), BG_TOP, BG_BOT)
    d = ImageDraw.Draw(img)
    cx = cy = S // 2
    draw_mark(d, cx, cy, int(S * 0.32), int(S * 0.056))
    img = draw_monogram(img, cx, cy, int(S * 0.42))
    img = img.resize((size, size), Image.LANCZOS)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0), rounded_mask((size, size), radius))
    return out


def make_banner(w=1500, h=400):
    S = 2
    W, H = w * S, h * S
    img = vgrad((W, H), BG_TOP, BG_BOT)
    # subtle right-side glow accent
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([W * 0.55, -H * 0.4, W * 1.25, H * 0.9], fill=(120, 60, 220, 60))
    glow = glow.filter(ImageFilter.GaussianBlur(W * 0.04))
    img = Image.alpha_composite(img, glow)

    # mark
    d = ImageDraw.Draw(img)
    mx, my, mR, mW = int(W * 0.145), H // 2, int(H * 0.36), int(H * 0.062)
    draw_mark(d, mx, my, mR, mW)
    img = draw_monogram(img, mx, my, int(H * 0.50))

    # wordmark
    d = ImageDraw.Draw(img)
    x0 = int(W * 0.28)
    f_title = ImageFont.truetype(BOLD, int(H * 0.27))
    f_sub = ImageFont.truetype(SEMI, int(H * 0.135))
    f_tag = ImageFont.truetype(REG, int(H * 0.075))
    f_ru = ImageFont.truetype(REG, int(H * 0.062))

    d.text((x0, int(H * 0.16)), "BROADER", font=f_title, fill=WHITE)
    # accent dot after title
    tbbox = d.textbbox((x0, int(H * 0.16)), "BROADER", font=f_title)
    d.text((tbbox[2] + int(H * 0.03), int(H * 0.20)), "БРОДЕРСТВО", font=f_sub, fill=MUTED)

    d.text((x0, int(H * 0.56)), "Buy if you can  ·  Broad if you can't  ·  Pay, or Broad something of your own",
           font=f_tag, fill=WHITE)
    d.text((x0, int(H * 0.72)), "Купи, если можешь · Бродь, если не можешь · Заплати, либо забродь что-то своё",
           font=f_ru, fill=MUTED)

    img = img.resize((w, h), Image.LANCZOS)
    return img


def make_og(w=1200, h=630):
    S = 2
    W, H = w * S, h * S
    img = vgrad((W, H), BG_TOP, BG_BOT)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([W * 0.3, H * 0.02, W * 0.7, H * 0.52], fill=(120, 60, 220, 70))
    glow = glow.filter(ImageFilter.GaussianBlur(W * 0.04))
    img = Image.alpha_composite(img, glow)

    d = ImageDraw.Draw(img)
    cx, cy = W // 2, int(H * 0.30)
    draw_mark(d, cx, cy, int(H * 0.245), int(H * 0.042))
    img = draw_monogram(img, cx, cy, int(H * 0.34))

    d = ImageDraw.Draw(img)
    f_title = ImageFont.truetype(BOLD, int(H * 0.115))
    f_sub = ImageFont.truetype(SEMI, int(H * 0.065))
    f_tag = ImageFont.truetype(REG, int(H * 0.042))

    d.text((cx, int(H * 0.66)), "The Broader Movement", font=f_title, fill=WHITE, anchor="mm")
    d.text((cx, int(H * 0.77)), "БРОДЕРСТВО", font=f_sub, fill=MUTED, anchor="mm")
    d.text((cx, int(H * 0.875)), "Buy if you can · Broad if you can't · Pay, or Broad something of your own",
           font=f_tag, fill=(225, 218, 245, 255), anchor="mm")

    img = img.resize((w, h), Image.LANCZOS)
    return img


def make_favicon(size=64):
    S = size * 8
    img = vgrad((S, S), BG_TOP, BG_BOT)
    d = ImageDraw.Draw(img)
    cx = cy = S // 2
    draw_mark(d, cx, cy, int(S * 0.34), int(S * 0.07))
    img = img.resize((size, size), Image.LANCZOS)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0), rounded_mask((size, size), size // 5))
    return out


def main():
    make_logo(1024).save(os.path.join(OUT, "logo.png"))
    make_icon(512).save(os.path.join(OUT, "icon-512.png"))
    make_banner(1500, 400).save(os.path.join(OUT, "banner.png"))
    make_og(1200, 630).save(os.path.join(OUT, "og-image.png"))
    make_favicon(64).save(os.path.join(OUT, "favicon-64.png"))
    print("wrote:", os.listdir(OUT))


if __name__ == "__main__":
    main()
