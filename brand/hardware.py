# Draws brand/hardware-illustration.png and src/assets/hardware.png: an original illustration of the instrument's
# panel layout (no vendor logos, model names or photos) with the app's real home screen on its display.
# Run from the repo root.
import colorsys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

S = 2  # supersampling
W, H = 2000 * S, 1200 * S
img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


def font(px):
    return ImageFont.truetype(BOLD, px * S)


def R(x0, y0, x1, y1, r, fill=None, outline=None, width=0):
    d.rounded_rectangle([x0 * S, y0 * S, x1 * S, y1 * S], radius=r * S, fill=fill, outline=outline, width=width * S)


def C(cx, cy, r, fill=None, outline=None, width=0):
    d.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S], fill=fill, outline=outline, width=width * S)


def T(x, y, text, px=17, fill='#e6e8eb', anchor='mm'):
    d.text((x * S, y * S), text, font=font(px), fill=fill, anchor=anchor)


def knob(cx, cy, r, ticks=False, pointer=True):
    if ticks:
        for a in range(-135, 136, 45):
            import math
            t = math.radians(a - 90)
            C(cx + math.cos(t) * (r + 14), cy + math.sin(t) * (r + 14), 2.5, fill='#e6e8eb')
    C(cx, cy + 4, r + 2, fill='#050506')
    C(cx, cy, r, fill='#2a2c30')
    C(cx, cy, r - 6, fill='#1b1c1f', outline='#3b3e44', width=2)
    if pointer:  # potentiometers have a pointer line; endless encoders do not
        d.line([cx * S, cy * S, cx * S, (cy - r + 8) * S], fill='#f2f3f5', width=5 * S)


def glow_pad(x0, y0, x1, y1, rgb, r=10):
    """A lit rubber pad: saturated edge, bright centre."""
    w, h = (x1 - x0) * S, (y1 - y0) * S
    pad = Image.new('RGBA', (w, h), rgb + (255,))
    hi = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(hi).ellipse([w * .15, h * .15, w * .85, h * .85], fill=(255, 255, 255, 120))
    pad.alpha_composite(hi.filter(ImageFilter.GaussianBlur(min(w, h) * .18)))
    mask = Image.new('L', (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], radius=r * S, fill=255)
    R(x0 - 3, y0 - 3, x1 + 3, y1 + 5, r + 2, fill='#050506')
    img.paste(pad, (x0 * S, y0 * S), mask)


def hue(hdeg, s=.75, v=1.0):
    r, g, b = colorsys.hsv_to_rgb(hdeg / 360, s, v)
    return (int(r * 255), int(g * 255), int(b * 255))


# body: black, with a faint brushed texture
shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
ImageDraw.Draw(shadow).rounded_rectangle([20 * S, 70 * S, 1980 * S, 1190 * S], radius=24 * S, fill=(0, 0, 0, 160))
img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(18 * S)))
R(0, 45, 2000, 1185, 18, fill='#0d0e10')
R(8, 50, 1992, 1105, 14, fill='#18191c')
brush = Image.new('RGBA', (W, H), (0, 0, 0, 0))
bd = ImageDraw.Draw(brush)
import random
random.seed(7)
for y in range(52 * S, 1104 * S, 3):
    bd.line([(10 * S, y), (1990 * S, y)], fill=(255, 255, 255, random.randint(0, 7)))
img.alpha_composite(brush)

# filter section
d.line([272 * S, 110 * S, 272 * S, 230 * S], fill='#d8dadd', width=2 * S)
for seg in [(272, 460), (575, 810), (915, 935)]:
    d.line([seg[0] * S, 110 * S, seg[1] * S, 110 * S], fill='#d8dadd', width=2 * S)
d.line([935 * S, 110 * S, 935 * S, 230 * S], fill='#d8dadd', width=2 * S)
d.line([272 * S, 230 * S, 935 * S, 230 * S], fill='#d8dadd', width=2 * S)
d.line([778 * S, 125 * S, 778 * S, 225 * S], fill='#d8dadd', width=2 * S)
T(517, 110, 'LOW PASS', 17); T(863, 110, 'HIGH PASS', 17)
T(162, 111, 'MAIN OUT', 16)
knob(162, 168, 34, ticks=True)
for x, label in [(340, 'DRIVE'), (515, 'CUTOFF'), (690, 'RESONANCE'), (865, 'CUTOFF')]:
    knob(x, 165, 32, ticks=True)
    T(x, 218, label, 16)
R(418, 162, 442, 170, 2, fill='#f7b83d'); T(430, 186, 'OVER', 14)
C(978, 168, 20, fill='#2a2c30'); C(978, 168, 13, fill='#c4252b'); T(978, 218, 'ACTIVE', 16)

# touch strip section
R(105, 255, 219, 912, 6, fill='#0a0b0c')  # section panel, centre x = 162
R(124, 268, 200, 312, 6, fill='#2a2c30', outline='#9fa3a9', width=2); T(162, 290, 'MODE', 16)
for i, (m, c) in enumerate([('PITCH', '#4add8c'), ('REPEAT', '#4add8c'), ('USER1', '#9db8ff'), ('USER2', '#9db8ff')]):
    T(162, 351 + i * 26, m, 15, fill=c)
R(124, 468, 200, 512, 6, fill='#2a2c30', outline='#e6e8eb', width=3); T(162, 490, 'HOLD', 16)
# the strip, inset by the same margin as the buttons, and its 16 LEDs centred inside it with equal top/bottom margins
st0, st1 = 534, 893
R(119, st0, 205, st1, 6, fill='#141517', outline='#3b3e44', width=2)
n, gap, margin = 16, 6, 16
led = ((st1 - st0) - 2 * margin - (n - 1) * gap) / n
for i in range(n):
    y = st0 + margin + i * (led + gap)
    R(156, y, 168, y + led, 2, fill='#2b6cff' if i >= 6 else '#16223f')

# 4 x 4 pads
xs, ys, pw, ph = [272, 445, 619, 793], [258, 400, 542, 684], 142, 112
rows = [[290, 300, 315, 330], [185, 195, 205, 225], [58, 85, 125, 165], [0, 30, 45, 52]]
for r_, y in enumerate(ys):
    for c_, x in enumerate(xs):
        n = (3 - r_) * 4 + c_ + 1
        T(x + 2, y - 13, str(n), 16, anchor='lm')
        glow_pad(x, y, x + pw, y + ph, hue(rows[r_][c_], .72))

# pad mode buttons
for x, label in zip(xs, ['TRACK', 'MUTE', 'SLICE', 'SCALE']):
    R(x, 840, x + pw, 882, 5, fill='#e6e8eb'); R(x + 4, 844, x + pw - 4, 878, 3, fill='#0d0e10'); T(x + pw / 2, 861, label, 16)

# display with the app's home screen
R(1020, 255, 1752, 678, 8, fill='#2a2c30')
R(1030, 265, 1742, 668, 6, fill='#050506')
sw, sh = 665, 399
sx0, sy0 = 1386 - sw // 2, 267
shot = Image.open('src/assets/screens/home.png').convert('RGBA').resize((sw * S, sh * S), Image.LANCZOS)
img.alpha_composite(shot, (sx0 * S, sy0 * S))

# six encoders under the display
for i in range(6):
    knob(1083 + i * 121.5, 758, 40, pointer=False)
    C(1083 + i * 121.5, 758, 44, outline='#3b3e44', width=3)

# right column: USB port, USB STOP, BACK / HOME, selector
R(1815, 128, 1910, 245, 6, fill='#2a2c30'); R(1822, 140, 1903, 200, 4, fill='#050506'); R(1840, 216, 1888, 224, 3, fill='#4add8c')
C(1700, 168, 24, fill='#2a2c30'); C(1700, 168, 14, fill='#c4252b'); T(1700, 123, '— USB STOP', 15)
T(1835, 274, 'BACK', 16); T(1912, 274, 'HOME', 16)
R(1800, 298, 1858, 328, 14, fill='#2a2c30'); C(1914, 313, 16, fill='#2a2c30')
C(1862, 470, 72, fill='#050506', outline='#e6e8eb', width=3)
knob(1862, 470, 56, pointer=False)  # the selector is an encoder too

# transport row
def button(cx, label, border='#e6e8eb', fill='#0d0e10', w=46):
    R(cx - w, 840, cx + w, 882, 5, fill=border); R(cx - w + 4, 844, cx + w - 4, 878, 3, fill=fill)
    if label:
        T(cx, 861, label, 16)
button(1083, 'SHIFT', border='#9fa3a9', fill='#2a2c30', w=44)
button(1260, '', border='#e2343a'); C(1260, 861, 9, fill='#e2343a')
button(1387, ''); R(1379, 853, 1395, 869, 1, fill='#e6e8eb')
button(1515, '', border='#3bd16f')
d.polygon([(1506 * S, 851 * S), (1506 * S, 871 * S), (1526 * S, 861 * S)], fill='#3bd16f')
button(1691, 'SCENE', w=46)
button(1862, 'PATTERN', w=46)
R(1816, 893, 1908, 913, 2, fill='#e6e8eb'); T(1862, 903, 'LENGTH', 14, fill='#0d0e10')

# 16 step keys and 4 bar keys
for i in range(16):
    x = 112 + i * 92
    T(x + 32, 953, str(i + 1), 16)
    if i % 4 == 0:
        R(x, 943, x + 64, 962, 2, outline='#e6e8eb', width=2)
    glow_pad(x, 972, x + 64, 1085, hue([45, 95, 225, 320][i % 4] + i * 3, .45, .95), r=6)
for j in range(4):
    x = 1643 + j * 72
    T(x + 26, 953, str(j + 1), 16)
    R(x, 972, x + 52, 981, 2, fill='#3bd16f')
    glow_pad(x, 1003, x + 52, 1085, (70, 150, 255), r=6)

out = img.resize((W // S, H // S), Image.LANCZOS)
out.save('src/assets/hardware.png')
out.save('brand/hardware-illustration.png')
