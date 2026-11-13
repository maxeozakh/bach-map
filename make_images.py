"""Resize the downloaded images for the web: img/t/ holds card thumbnails, img/p/ the larger panel images, both WebP.
A card shows its image at 38x50 css px and can be zoomed to 2.5x, so thumbnails cover 152x200 (2.5x at 2x density, rounded
down). The panel shows 140 css px wide. Animated GIFs get a still thumbnail. Only images newer than their output are redone."""
import os
from PIL import Image, ImageFile, ImageSequence

ImageFile.LOAD_TRUNCATED_IMAGES = True   # a few downloaded GIFs end a few bytes short; browsers show them anyway

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "img")
SIZES = {"t": (152, 200), "p": (420, None)}   # (width, height to cover); None = width only


def fit(im, w, h):
    s = max(w / im.width, h / im.height) if h else w / im.width
    s = min(s, 1)
    return im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)


def convert(src, dst, w, h, still=False):
    im = Image.open(src)
    frames = getattr(im, "n_frames", 1)
    if frames > 1 and not still:
        seq, dur = [], []
        for f in ImageSequence.Iterator(im):
            seq.append(fit(f.convert("RGBA"), w, h)); dur.append(f.info.get("duration", 80))
        seq[0].save(dst, "WEBP", save_all=True, append_images=seq[1:], duration=dur, loop=0, quality=60, method=6)
    else:
        im = im.convert("RGBA") if im.mode in ("P", "LA", "RGBA") else im.convert("RGB")
        fit(im, w, h).save(dst, "WEBP", quality=78, method=6)


def run():
    done = 0
    for d in SIZES: os.makedirs(os.path.join(SRC, d), exist_ok=True)
    for f in sorted(os.listdir(SRC)):
        src = os.path.join(SRC, f)
        if not os.path.isfile(src) or f.startswith("."): continue
        for d, (w, h) in SIZES.items():
            dst = os.path.join(SRC, d, os.path.splitext(f)[0] + ".webp")
            if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src): continue
            convert(src, dst, w, h, still=d == "t"); done += 1   # animations play only in the panel
    return done


if __name__ == "__main__":
    print(run(), "images written")
