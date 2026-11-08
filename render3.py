"""Kitchen Ticket renderer (v3). Every slide is a restaurant order ticket on a dark counter."""
from PIL import Image, ImageDraw, ImageFont
import os

FD = "/home/user/workspace/hidden_menu/fonts3/"
PAPER = (250, 249, 244); COUNTER = (46, 48, 52); INK = (22, 22, 22); RED = (206, 34, 30); GREY = (112, 112, 112)
_cache = {}


def mono(size, w=500):
    key = (int(size), w)
    if key not in _cache:
        f = ImageFont.truetype(FD + "MartianMono.ttf", int(size))
        try:
            ax = {"Weight": w, "Width": 75}
            f.set_variation_by_axes([ax.get(a["name"].decode(), a["default"]) for a in f.get_variation_axes()])
        except Exception:
            pass
        _cache[key] = f
    return _cache[key]


def wrap(d, t, f, mw):
    out = []
    for para in t.split("\n"):
        c = ""
        for w in para.split():
            x = (c + " " + w).strip()
            if d.textlength(x, font=f) <= mw:
                c = x
            else:
                if c:
                    out.append(c)
                c = w
        out.append(c)
    return out


def grain(im, a=0.04):
    n = Image.effect_noise(im.size, 40).convert("L")
    return Image.blend(im.convert("RGB"), Image.merge("RGB", (n, n, n)), a)


def ticket(w, h, day=None, clock="7:42P"):
    im = Image.new("RGBA", (w, h), PAPER + (255,)); d = ImageDraw.Draw(im)
    for x in range(0, w, 26):
        d.polygon([(x, h), (x + 13, h - 16), (x + 26, h)], fill=(0, 0, 0, 0))
        d.polygon([(x, 0), (x + 13, 16), (x + 26, 0)], fill=(0, 0, 0, 0))
    if day is not None:
        d.text((50, 50), f"TBL {day:02d}   GUESTS 2   SRV HM", font=mono(26, 600), fill=INK)
        d.text((w - 50, 50), clock, font=mono(26, 600), fill=INK, anchor="ra")
        d.line((50, 100, w - 50, 100), fill=INK, width=3)
    return im, d


def stamp(txt, size=96, rot=-11):
    f = mono(size, 800); tw = int(ImageDraw.Draw(Image.new("L", (1, 1))).textlength(txt, font=f))
    s = Image.new("RGBA", (tw + 80, size + 70), (0, 0, 0, 0)); sd = ImageDraw.Draw(s)
    sd.rounded_rectangle((5, 5, tw + 75, size + 65), 16, outline=RED + (225,), width=9)
    sd.text(((tw + 80) // 2, (size + 70) // 2), txt, font=f, fill=RED + (225,), anchor="mm")
    return s.rotate(rot, expand=True, resample=Image.BICUBIC)


class Flow:
    """Lays out text top to bottom. dry=True only measures."""

    def __init__(self, d, x0=50, x1=850, y=150, k=1.0, dry=False):
        self.d, self.x0, self.x1, self.y, self.k, self.dry = d, x0, x1, y, k, dry

    def text(self, t, size, w=500, fill=INK, lh=1.32, gap=0, upper=False, indent=0):
        self.y += gap * self.k
        f = mono(size * self.k, w); t = t.upper() if upper else t
        for line in wrap(self.d, t, f, self.x1 - self.x0 - indent):
            if not self.dry:
                self.d.text((self.x0 + indent, self.y), line, font=f, fill=fill)
            self.y += size * self.k * lh

    def label(self, t, gap=0):
        self.text(f"** {t} **", 30, 700, RED, gap=gap, upper=True)
        self.y += 18 * self.k

    def rule(self, gap=30):
        self.y += gap * self.k
        if not self.dry:
            self.d.line((self.x0, self.y, self.x1, self.y), fill=INK, width=2)
        self.y += gap * self.k

    def row(self, a, b, size=32, gap=0):
        self.y += gap * self.k
        f = mono(size * self.k, 500); fb = mono(size * self.k, 700)
        bw = self.d.textlength(b, font=fb) if b else 0
        lines = wrap(self.d, a, f, self.x1 - self.x0 - bw - 30)
        for i, line in enumerate(lines):
            if not self.dry:
                self.d.text((self.x0, self.y), line, font=f, fill=INK)
                if i == 0 and b:
                    self.d.text((self.x1, self.y), b, font=fb, fill=RED, anchor="ra")
            self.y += size * self.k * 1.45


BOTTOM = 1110


def lay(d, s, fl):
    t = s["t"]
    if t == "cover":
        fl.y = 165
        fl.text(s["head"], 70, 800, INK, lh=1.25, upper=True)
        if s.get("punch"):
            fl.text(s["punch"], 70, 800, RED, lh=1.25, upper=True, gap=26)
        if s.get("voids"):
            fl.rule(34)
            for v in s["voids"]:
                fl.row("1x " + v, "VOID", 32)
    elif t == "note":
        fl.label(s["label"])
        fl.text(s["lead"], 50, 700, INK, gap=10)
        if s.get("body"):
            fl.text(s["body"], 44, 400, INK, gap=30)
        if s.get("src"):
            fl.rule(34)
            fl.text("SOURCE: " + s["src"], 25, 500, GREY, lh=1.5, upper=True)
    elif t == "big":
        fl.label(s["label"])
        fl.text(s["num"], s.get("numsize", 190), 800, RED, lh=1.1, gap=0)
        fl.text(s["lead"], 46, 700, INK, gap=16)
        if s.get("body"):
            fl.text(s["body"], 40, 400, INK, gap=26)
        if s.get("src"):
            fl.rule(30)
            fl.text("SOURCE: " + s["src"], 25, 500, GREY, lh=1.5, upper=True)
    elif t == "rows":
        fl.label(s["label"])
        if s.get("title"):
            fl.text(s["title"], 52, 800, INK, upper=True, lh=1.22)
        fl.rule(30)
        for a, b in s["rows"]:
            fl.text(a, 40, 700, INK, gap=8)
            if b:
                fl.text(">> " + b, 34, 400, GREY, indent=0, gap=4)
            fl.y += 22 * fl.k
    elif t == "vs":
        fl.label(s["label"])
        if s.get("title"):
            fl.text(s["title"], 46, 700, INK, gap=0)
            fl.y += 20 * fl.k
        for i, side in enumerate((s["a"], s["b"])):
            fl.rule(26)
            fl.text(f"SEAT {i + 1}  /  {side[0]}", 28, 700, RED if side[3] else GREY, upper=True)
            fl.text(side[1], 64, 800, INK, gap=10, lh=1.2)
            fl.text(side[2], 38, 400, INK, gap=8)
    elif t == "tip":
        fl.label(s.get("label", "Note from the kitchen"))
        fl.text(s["title"], 80, 800, INK, upper=True, lh=1.18, gap=6)
        fl.text(s["body"], 44, 400, INK, gap=34)
        if s.get("box"):
            fl.y += 50 * fl.k
            top = fl.y
            f = mono(34 * fl.k, 700)
            lines = wrap(d, s["box"].upper(), f, fl.x1 - fl.x0 - 60)
            h = len(lines) * 34 * fl.k * 1.4 + 56 * fl.k
            if not fl.dry:
                d.rectangle((fl.x0, top, fl.x1, top + h), outline=RED, width=4)
                yy = top + 28 * fl.k
                for line in lines:
                    d.text(((fl.x0 + fl.x1) / 2, yy), line, font=f, fill=RED, anchor="ma"); yy += 34 * fl.k * 1.4
            fl.y = top + h
    elif t == "end":
        fl.label(s.get("label", "Before you go"))
        fl.text(s["title"], 66, 800, INK, upper=True, lh=1.22)
        if s.get("body"):
            fl.text(s["body"], 42, 400, INK, gap=30)
        fl.y += 60 * fl.k
        top = fl.y; h = 250 * fl.k
        if not fl.dry:
            d.rectangle((fl.x0, top, fl.x1, top + h), fill=INK)
            d.text(((fl.x0 + fl.x1) / 2, top + 38 * fl.k), "COMMENT", font=mono(34 * fl.k, 600), fill=PAPER, anchor="ma")
            d.text(((fl.x0 + fl.x1) / 2, top + 92 * fl.k), "MENU", font=mono(110 * fl.k, 800), fill=PAPER, anchor="ma")
        fl.y = top + h
        fl.text("and I'll DM you the free cheat sheet: 10 things to look for on any menu.", 34, 500, INK, gap=26)


def render_slide(s, day, n, total, clock):
    im = Image.new("RGB", (1080, 1350), COUNTER)
    t, d = ticket(900, 1290, day, clock)
    start = 150
    k = 1.32 if s["t"] in ("cover", "note", "tip") else 1.3
    for _ in range(24):
        fl = Flow(d, y=start, k=k, dry=True); lay(d, s, fl)
        extra = 230 if (s["t"] == "cover" and s.get("stamp")) else (260 if s["t"] == "cover" else 0)
        if fl.y + extra <= BOTTOM:
            break
        k *= 0.94
    fl = Flow(d, y=start, k=k); lay(d, s, fl)
    if s["t"] == "cover" and s.get("stamp"):
        st = stamp(s["stamp"], 96)
        t.paste(st, (850 - st.width + 10, int(min(fl.y + 40, BOTTOM - st.height + 40))), st)
    if s["t"] == "cover" and not s.get("stamp"):
        barcode(d, day)
    if s["t"] == "cover":
        d.text((50, 1170), "@thehiddenmenu.io", font=mono(26, 500), fill=GREY)
        d.text((850, 1170), "SWIPE >>", font=mono(26, 700), fill=INK, anchor="ra")
    else:
        d.text((50, 1170), "THE HIDDEN MENU", font=mono(26, 500), fill=GREY)
        d.text((850, 1170), f"{n} / {total}", font=mono(26, 700), fill=INK, anchor="ra")
    im.paste(t, (90, 30), t)
    return grain(im)


def barcode(d, day):
    import random
    r = random.Random(day)
    y0, y1 = 960, 1080
    d.line((50, 920, 850, 920), fill=INK, width=2)
    d.text((50, 935), f"ORDER #{day:04d}", font=mono(24, 600), fill=GREY)
    d.text((850, 935), "SERVED", font=mono(24, 600), fill=GREY, anchor="ra")
    x = 50
    y0 = 980
    while x < 850:
        w = r.choice((3, 3, 5, 8)); d.rectangle((x, y0, x + w, y1), fill=INK); x += w + r.choice((4, 6, 9))


def clock_for(day):
    m = (day * 37) % 60
    h = 5 + (day * 5) % 5
    return f"{h}:{m:02d}P"


def carousel(folder, slides, day):
    os.makedirs(folder, exist_ok=True)
    for f in os.listdir(folder):
        if f.startswith("slide_"):
            os.remove(os.path.join(folder, f))
    for i, s in enumerate(slides, 1):
        render_slide(s, day, i, len(slides), clock_for(day)).save(f"{folder}/slide_{i:02d}.png")
