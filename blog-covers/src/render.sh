#!/bin/bash
CHR=/opt/pw-browsers/chromium-1194/chrome-linux/chrome
$CHR --headless=new --no-sandbox --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=2 --window-size=1240,760 \
  --screenshot="$2.raw.png" "$1" >/dev/null 2>&1
python3 - "$2" <<'PY'
import sys
from PIL import Image
out=sys.argv[1]
im=Image.open(out+'.raw.png').convert('RGB')
px=im.load(); W,H=im.size
S=(255,0,255)
def col_ok(x):  return any(px[x,y]!=S for y in range(0,H,4))
def row_ok(y):  return any(px[x,y]!=S for x in range(0,W,4))
x0=next(x for x in range(W) if col_ok(x)); x1=next(x for x in range(W-1,-1,-1) if col_ok(x))
y0=next(y for y in range(H) if row_ok(y)); y1=next(y for y in range(H-1,-1,-1) if row_ok(y))
im.crop((x0,y0,x1+1,y1+1)).resize((2400,1260),Image.LANCZOS).save(out)
print('stage bbox',(x0,y0,x1+1,y1+1))
PY
rm -f "$2.raw.png"
