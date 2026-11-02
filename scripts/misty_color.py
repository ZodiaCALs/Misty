# SPDX-FileCopyrightText: 2026 ZodiaCALs
# SPDX-License-Identifier: Apache-2.0
"""Misty's reference colour conversion: OKLCH to sRGB, clipped per channel.

Every platform package implements these same steps, so a hue chosen on one
device renders the same on every other. Browsers clip out-of-gamut channels
the same way when they draw to an sRGB display.
"""
import math


def _encode(v):
    return 12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055


def oklch_to_srgb(l, c, h):
    """Return (r, g, b) in 0..1 for an OKLCH colour; h is in degrees."""
    angle = math.radians(h % 360)
    a, b = c * math.cos(angle), c * math.sin(angle)
    l3 = (l + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m3 = (l - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s3 = (l - 0.0894841775 * a - 1.2914855480 * b) ** 3
    linear = (
        4.0767416621 * l3 - 3.3077115913 * m3 + 0.2309699292 * s3,
        -1.2684380046 * l3 + 2.6097574011 * m3 - 0.3413193965 * s3,
        -0.0041960863 * l3 - 0.7034186147 * m3 + 1.7076147010 * s3,
    )
    return tuple(min(1.0, max(0.0, _encode(v))) for v in linear)


def to_8bit(rgb):
    """Round each channel half up to 0..255, as every package does."""
    return tuple(int(math.floor(v * 255 + 0.5)) for v in rgb)


def to_hex(rgb):
    return "#" + "".join(f"{v:02x}" for v in to_8bit(rgb))


def resolve(defn, hue):
    """Resolve a colour definition from the token file at a hue.

    defn is {"l", "c", "h", "alpha", "hue"}; when "hue" is "relative", "h" is
    an offset from the hue. Returns (r, g, b, alpha) with 8-bit channels.
    """
    h = hue + defn["h"] if defn["hue"] == "relative" else defn["h"]
    return to_8bit(oklch_to_srgb(defn["l"], defn["c"], h)) + (defn["alpha"],)
