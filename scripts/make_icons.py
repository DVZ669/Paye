#!/usr/bin/env python3
"""Génère les icônes PNG de l'app BENCH (barbell) à partir d'un rendu vectoriel.
Fond sombre #0b0d12, accent dégradé orange->or (#e8583a -> #f0a83a)."""
import os
from PIL import Image, ImageDraw

BG = (11, 13, 18)      # #0b0d12
ACC = (232, 88, 58)    # #e8583a
GOLD = (240, 168, 58)  # #f0a83a
INK = (238, 241, 246)  # #eef1f6

OUT = os.path.join(os.path.dirname(__file__), "..", "icons")
os.makedirs(OUT, exist_ok=True)

SS = 4  # supersampling


def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def rounded_mask(size, radius):
    m = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=255)
    return m


def draw_barbell(draw, cx, cy, S, scale=1.0):
    """Dessine une barre d'haltères horizontale centrée sur (cx, cy)."""
    unit = S * scale
    # barre centrale
    bar_h = unit * 0.085
    bar_w = unit * 0.66
    draw.rounded_rectangle(
        [cx - bar_w / 2, cy - bar_h / 2, cx + bar_w / 2, cy + bar_h / 2],
        radius=bar_h / 2, fill=INK)

    # plaques : paires symétriques (interne haute, externe basse)
    plate_defs = [
        (0.30, 0.42, 0.055, GOLD),   # plaque interne (grande)
        (0.30, 0.42, 0.055, GOLD),
        (0.40, 0.30, 0.05, ACC),     # plaque externe (moyenne)
        (0.40, 0.30, 0.05, ACC),
    ]
    # gauche et droite
    for side in (-1, 1):
        # interne
        x = cx + side * unit * 0.30
        ph = unit * 0.44
        pw = unit * 0.055
        col = lerp(ACC, GOLD, 0.35)
        draw.rounded_rectangle(
            [x - pw, cy - ph / 2, x + pw, cy + ph / 2],
            radius=pw * 0.6, fill=col)
        # externe
        x2 = cx + side * unit * 0.40
        ph2 = unit * 0.30
        pw2 = unit * 0.05
        col2 = lerp(ACC, GOLD, 0.05)
        draw.rounded_rectangle(
            [x2 - pw2, cy - ph2 / 2, x2 + pw2, cy + ph2 / 2],
            radius=pw2 * 0.6, fill=col2)
        # embout
        x3 = cx + side * unit * 0.47
        draw.rounded_rectangle(
            [x3 - unit * 0.02, cy - unit * 0.06, x3 + unit * 0.02, cy + unit * 0.06],
            radius=unit * 0.02, fill=INK)


def make(size, maskable=False, path=None):
    S = size * SS
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # fond
    if maskable:
        d.rectangle([0, 0, S, S], fill=BG + (255,))
        scale = 0.80
    else:
        d.rounded_rectangle([0, 0, S - 1, S - 1], radius=S * 0.22, fill=BG + (255,))
        scale = 1.0

    # barre d'haltères centrée
    draw_barbell(d, S / 2, S * 0.50, S, scale=scale)

    img = img.resize((size, size), Image.LANCZOS)

    if not maskable:
        mask = rounded_mask(size, int(size * 0.22))
        img.putalpha(mask)

    if path:
        img.save(path)
    return img


make(512, maskable=False, path=os.path.join(OUT, "icon-512.png"))
make(192, maskable=False, path=os.path.join(OUT, "icon-192.png"))
make(180, maskable=False, path=os.path.join(OUT, "icon-180.png"))
make(32, maskable=False, path=os.path.join(OUT, "icon-32.png"))
make(512, maskable=True, path=os.path.join(OUT, "icon-512-maskable.png"))
make(192, maskable=True, path=os.path.join(OUT, "icon-192-maskable.png"))
print("icons written to", os.path.abspath(OUT))
