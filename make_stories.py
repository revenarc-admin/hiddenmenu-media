import sys, os
sys.path.insert(0, "/home/user/workspace/hidden_menu")
from PIL import Image, ImageDraw, ImageFilter
import render3 as R
from content_v3 import P
W, H = 1080, 1920
def story(day):
    folder = P[day][0]
    im = Image.new("RGB", (W, H), R.COUNTER); d = ImageDraw.Draw(im)
    d.text((W // 2, 150), f"NEW ON THE RAIL  /  NO. {day:02d}", font=R.mono(34, 700), fill=R.PAPER, anchor="mm")
    cv = Image.open(f"carousels/{folder}/slide_01.png").convert("RGB")
    cw = 960; ch = int(cv.height * cw / cv.width); cv = cv.resize((cw, ch), Image.LANCZOS)
    x, y = (W - cw) // 2, 250
    im.paste(cv, (x, y))
    ty = y + ch + 90
    d.text((W // 2, ty), "Tap through. It's on my profile.", font=R.mono(40, 500), fill=R.PAPER, anchor="mm")
    d.text((W // 2, ty + 70), "@thehiddenmenu.io", font=R.mono(34, 700), fill=(236, 120, 110), anchor="mm")
    os.makedirs("stories", exist_ok=True)
    out = f"stories/day{day:02d}.jpg"; R.grain(im, 0.03).save(out, quality=92); return out
if __name__ == "__main__":
    days = [int(a) for a in sys.argv[1:]] or sorted(P)
    for dd in days: story(dd)
    print("ok", len(days))
