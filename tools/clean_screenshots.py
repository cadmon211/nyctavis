"""Clean NYCTAVIS screenshots for the website / Microsoft Store.

- Removes the Windows taskbar (bottom strip).
- Optionally blurs rectangles (e.g. folder paths) so they can't be read.

Usage:
  python tools/clean_screenshots.py INPUT.png OUTPUT.png
  python tools/clean_screenshots.py INPUT.png OUTPUT.png --blur x0,y0,x1,y1 [--blur ...]

Coordinates are pixels on the ORIGINAL image (1920x1080 for these captures).
"""
import argparse
from PIL import Image, ImageFilter

TASKBAR_PX = 48  # Windows 11 taskbar height at 1080p

def clean(src, dst, rects, taskbar=TASKBAR_PX):
    im = Image.open(src).convert("RGB")
    for (x0, y0, x1, y1) in rects:
        reg = im.crop((x0, y0, x1, y1))
        small = reg.resize((max(1, (x1 - x0) // 16), max(1, (y1 - y0) // 6)))
        reg = small.resize((x1 - x0, y1 - y0)).filter(ImageFilter.GaussianBlur(6))
        im.paste(reg, (x0, y0))
    w, h = im.size
    im.crop((0, 0, w, h - taskbar)).save(dst)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("dst")
    ap.add_argument("--blur", action="append", default=[], help="x0,y0,x1,y1")
    ap.add_argument("--taskbar", type=int, default=TASKBAR_PX)
    a = ap.parse_args()
    rects = [tuple(int(v) for v in b.split(",")) for b in a.blur]
    clean(a.src, a.dst, rects, a.taskbar)
    print("wrote", a.dst)

# For the localized Recommendations screenshots (ES/FR), the path rectangles
# are approximately (same layout, 1920x1080):
#   (428,850,968,880) (428,930,715,960) (1240,940,1815,966) (1240,966,1478,992)
