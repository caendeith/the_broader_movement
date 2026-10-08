import os

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "BROADER_SPEC.txt"))
W = 64  # inner width between the side bars


def center(s):
    pad = W - len(s)
    left = pad // 2
    right = pad - left
    return "|" + " " * left + s + " " * right + "|"


def left(s):
    return "|" + s + " " * (W - len(s)) + "|"


def rule(ch):
    return "+" + ch * W + "+"


def empty():
    return "|" + " " * W + "|"


lines = [
    rule("="),
    empty(),
    center("B R O A D E R   M O V E M E N T  .  B R O D E R S T V O"),
    empty(),
    center('"Buy if you can . Broad if you can\'t . Pay, or'),
    center('Broad something of your own."'),
    empty(),
    center('"Kupi, esli mozhesh . Brod\', esli ne mozhesh .'),
    center('Zaplati, libo zabrod\' chto-to svoe."'),
    empty(),
    rule("="),
    empty(),
    left("  TITLE    : [ Exact title / Tochnoe nazvanie ]"),
    left("  TYPE     : [ Film / Music / Game / Book / Software / Other ]"),
    left("  CREATOR  : [ Author / Studio / Artist -- always credit ]"),
    left("  YEAR     : [ Year of release ]"),
    left("  LANGUAGE : [ Audio / Subtitle languages ]"),
    left("  QUALITY  : [ Format / Resolution / Bitrate ]"),
    left("  SIZE     : [ Size ]"),
    left("  HASH     : [ SHA-256 / Checksum ]"),
    empty(),
    rule("-"),
    empty(),
    left("  This release is a BROAD, not a theft."),
    left("  Etot reliz -- BROD, a ne krazha."),
    empty(),
    left("  If you can afford it, BUY it officially."),
    left("  Esli mozhesh' -- KUPI oficial'no."),
    empty(),
    left("  If you can't, share it onward and keep the stream flowing."),
    left("  Esli net -- podelis' dal'she i sohrani potok."),
    empty(),
    left("  When you rise, pay -- or Broad something of your own:"),
    left("  buy the work, donate, or share your own creation."),
    left("  Kogda podnimesh'sya -- zaplati ili zabrod' chto-to svoe:"),
    left("  kupi, pozhertvuy, ili podelis' svoim."),
    empty(),
    rule("-"),
    empty(),
    left("  THE BROADER LOOP / CIKL BRODERA:"),
    empty(),
    left("    1. BUY if you can        . Kupi, esli mozhesh'"),
    left("    2. BROAD if you can't    . Brod', esli ne mozhesh'"),
    left("    3. PAY or BROAD          . Zaplati, libo zabrod'"),
    left("       something of your own   chto-to svoe"),
    empty(),
    rule("-"),
    empty(),
    left("  License   : BROADER PUBLIC LICENSE 1.0 (BPL-1.0)"),
    left("  Manifesto : BROADER_MANIFESTO.md"),
    left("  Community : #Broaders #Broderstvo #BroaderMovement"),
    empty(),
    rule("="),
]


def main():
    for ln in lines:
        assert len(ln) == W + 2, f"line length {len(ln)} != {W + 2}: {ln!r}"
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
