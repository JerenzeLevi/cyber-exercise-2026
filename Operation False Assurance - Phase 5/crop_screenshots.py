import os
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
SHOTS = os.path.join(BASE, "_screenshots")
OUT = os.path.join(SHOTS, "cropped")
os.makedirs(OUT, exist_ok=True)

# step1 "query" screenshots: keep header/query-bar/stats/timeline chart area only
STEP1_HEIGHT = 620

for f in sorted(os.listdir(SHOTS)):
    if not f.lower().endswith(".png"):
        continue
    if "step1" not in f:
        continue  # step2 evidence shots are already tight viewport captures
    path = os.path.join(SHOTS, f)
    im = Image.open(path)
    w, h = im.size
    crop_h = min(STEP1_HEIGHT, h)
    cropped = im.crop((0, 0, w, crop_h))
    out_path = os.path.join(SHOTS, f)  # overwrite in place
    cropped.save(out_path, dpi=(96, 96))
    print(f, "->", out_path, cropped.size)
