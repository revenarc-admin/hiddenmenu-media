import sys, os, glob, subprocess
sys.path.insert(0, "/home/user/workspace/hidden_menu")
from PIL import Image, ImageDraw
import render3 as R
from content_v3 import P
W, H = 1080, 1920
def frames(day):
    folder = P[day][0]
    bg = Image.new("RGB", (W, H), R.COUNTER)
    out = []
    slides = sorted(glob.glob(f"carousels/{folder}/slide_*.png"))
    os.makedirs(f"reels/tmp{day:02d}", exist_ok=True)
    for i, s in enumerate(slides):
        im = bg.copy(); d = ImageDraw.Draw(im)
        d.text((W//2, 230), f"THE HIDDEN MENU  /  NO. {day:02d}", font=R.mono(34, 700), fill=R.PAPER, anchor="mm")
        sl = Image.open(s).convert("RGB")
        sl = sl.resize((W, int(sl.height * W / sl.width)))
        y = (H - sl.height)//2 + 20
        im.paste(sl, (0, y))
        d.text((W//2, y + sl.height + 110), "@thehiddenmenu.io", font=R.mono(36, 700), fill=(236, 120, 110), anchor="mm")
        p = f"reels/tmp{day:02d}/f{i:02d}.png"; im.save(p); out.append(p)
    return out
def build(day):
    fr = frames(day); n = len(fr)
    dur = [3.6] + [3.0]*(n-2) + [3.6]; xf = 0.35
    args = ["ffmpeg","-y","-loglevel","error"]
    for p, t in zip(fr, dur): args += ["-loop","1","-t",str(t),"-i",p]
    total = sum(dur) - xf*(n-1)
    args += ["-f","lavfi","-t",str(total),"-i",
      "sine=f=220:sample_rate=44100,volume=0.05[a];sine=f=277.18,volume=0.04[b];sine=f=329.63,volume=0.04[c];[a][b][c]amix=3,lowpass=f=900,tremolo=f=0.25:d=0.4,afade=t=in:d=1.5,afade=t=out:st=%s:d=2" % (total-2)]
    fc = ""; last = "[0:v]"; off = 0
    for i in range(1, n):
        off += dur[i-1] - xf
        fc += f"{last}[{i}:v]xfade=transition=fade:duration={xf}:offset={off:.2f}[v{i}];"; last = f"[v{i}]"
    fc += f"{last}format=yuv420p[vout]"
    out = f"reels/day{day:02d}.mp4"
    args += ["-filter_complex", fc, "-map","[vout]","-map",f"{n}:a","-r","30","-c:v","libx264","-preset","medium","-crf","20","-c:a","aac","-b:a","128k","-shortest","-movflags","+faststart", out]
    subprocess.run(args, check=True); return out, total
if __name__ == "__main__":
    for d in [int(a) for a in sys.argv[1:]]: print(build(d))
