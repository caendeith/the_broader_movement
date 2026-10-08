import math, os

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets"))
os.makedirs(OUT, exist_ok=True)

VIOLET = "#8A2BE2"
PINK = "#FF4D8D"
GOLD = "#FFC24B"
WHITE = "#F6F2FF"
MUTED = "#ACA2D2"
BG_TOP = "#201546"
BG_BOT = "#090516"


def P(cx, cy, deg, r):
    a = math.radians(deg)
    return (cx + r * math.cos(a), cy + r * math.sin(a))


def f(v):
    return f"{v:.2f}"


def ring_segments(cx, cy, R, W):
    """Return SVG snippets for the 3-arc Broader Loop + arrowheads."""
    segs = [(0, 100, VIOLET), (120, 100, PINK), (240, 100, GOLD)]
    out = []
    for start, span, color in segs:
        end = start + span
        x1, y1 = P(cx, cy, start, R)
        x2, y2 = P(cx, cy, end, R)
        arc = (
            f'<path d="M {f(x1)} {f(y1)} A {f(R)} {f(R)} 0 0 1 {f(x2)} {f(y2)}" '
            f'fill="none" stroke="{color}" stroke-width="{W}"/>'
        )
        cap = f'<circle cx="{f(x1)}" cy="{f(y1)}" r="{f(W/2)}" fill="{color}"/>'
        # arrowhead at clockwise end
        e = math.radians(end)
        Tx, Ty = -math.sin(e), math.cos(e)
        Nx, Ny = math.cos(e), math.sin(e)
        L = W * 1.05
        hw = W * 0.72
        tip = (x2 + Tx * L, y2 + Ty * L)
        b1 = (x2 + Nx * hw, y2 + Ny * hw)
        b2 = (x2 - Nx * hw, y2 - Ny * hw)
        poly = (
            f'<polygon points="{f(tip[0])},{f(tip[1])} {f(b1[0])},{f(b1[1])} {f(b2[0])},{f(b2[1])}" '
            f'fill="{color}"/>'
        )
        out.append(arc + "\n  " + cap + "\n  " + poly)
    return "\n  ".join(out)


def grad_def(gid, top, bot):
    return (
        f'<linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bot}"/></linearGradient>'
    )


def glow_def(gid, color, opacity):
    return (
        f'<radialGradient id="{gid}" cx="0.5" cy="0.5" r="0.5">'
        f'<stop offset="0" stop-color="{color}" stop-opacity="{opacity}"/>'
        f'<stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient>'
    )


def monogram(cx, cy, size, fill=WHITE):
    return (
        f'<text x="{f(cx)}" y="{f(cy)}" font-family="Segoe UI, -apple-system, '
        f'Helvetica, Arial, sans-serif" font-weight="700" font-size="{f(size)}" '
        f'fill="{fill}" text-anchor="middle" dominant-baseline="central">B</text>'
    )


def make_logo_svg():
    cx = cy = 512.0
    R, W = 307.0, 51.0
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="1024" height="1024">
  <defs>
    {grad_def("bg", BG_TOP, BG_BOT)}
    {glow_def("glow", "#783CD2", "0.55")}
  </defs>
  <rect x="0" y="0" width="1024" height="1024" rx="210" fill="url(#bg)"/>
  <circle cx="{f(cx)}" cy="{f(cy)}" r="430" fill="url(#glow)"/>
  {ring_segments(cx, cy, R, W)}
  {monogram(cx, cy, 400)}
</svg>
'''


def make_icon_svg():
    cx = cy = 256.0
    R, W = 154.0, 26.0
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    {grad_def("bg", BG_TOP, BG_BOT)}
    {glow_def("glow", "#783CD2", "0.55")}
  </defs>
  <rect x="0" y="0" width="512" height="512" rx="110" fill="url(#bg)"/>
  <circle cx="{f(cx)}" cy="{f(cy)}" r="215" fill="url(#glow)"/>
  {ring_segments(cx, cy, R, W)}
  {monogram(cx, cy, 200)}
</svg>
'''


def make_favicon_svg():
    cx = cy = 32.0
    R, W = 26.0, 6.0
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>{grad_def("bg", BG_TOP, BG_BOT)}</defs>
  <rect x="0" y="0" width="64" height="64" rx="14" fill="url(#bg)"/>
  {ring_segments(cx, cy, R, W)}
</svg>
'''


def make_banner_svg():
    mx, my, mR, mW = 216.0, 200.0, 144.0, 25.0
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1500 400" width="1500" height="400">
  <defs>
    {grad_def("bg", BG_TOP, BG_BOT)}
    {glow_def("glow", "#783CD2", "0.5")}
  </defs>
  <rect x="0" y="0" width="1500" height="400" fill="url(#bg)"/>
  <circle cx="1050" cy="200" r="460" fill="url(#glow)"/>
  {ring_segments(mx, my, mR, mW)}
  {monogram(mx, my, 190)}
  <text x="420" y="150" font-family="Segoe UI, -apple-system, Helvetica, Arial, sans-serif"
        font-weight="700" font-size="108" fill="{WHITE}">BROADER</text>
  <text x="762" y="160" font-family="Segoe UI, -apple-system, Helvetica, Arial, sans-serif"
        font-weight="600" font-size="54" fill="{MUTED}">БРОДЕРСТВО</text>
  <text x="420" y="262" font-family="Segoe UI, -apple-system, Helvetica, Arial, sans-serif"
        font-weight="400" font-size="30" fill="{WHITE}">Buy if you can  ·  Broad if you can't  ·  Pay, or Broad something of your own</text>
  <text x="420" y="312" font-family="Segoe UI, -apple-system, Helvetica, Arial, sans-serif"
        font-weight="400" font-size="25" fill="{MUTED}">Купи, если можешь · Бродь, если не можешь · Заплати, либо забродь что-то своё</text>
</svg>
'''


def main():
    files = {
        "logo.svg": make_logo_svg(),
        "icon.svg": make_icon_svg(),
        "favicon.svg": make_favicon_svg(),
        "banner.svg": make_banner_svg(),
    }
    for name, content in files.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
            fh.write(content)
    print("wrote svg:", list(files))


if __name__ == "__main__":
    main()
