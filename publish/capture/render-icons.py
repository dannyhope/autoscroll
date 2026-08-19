#!/usr/bin/env python3
"""Rasterise icons/icon.svg geometry into toolbar PNGs (RGBA) and a store RGB icon."""
from __future__ import annotations

import struct
import sys
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GREY = (0x7B, 0x85, 0x8A)
# 12% inset on a unit square; two downward triangles, gap between them.
PAD = 0.12
GAP = 0.06
TOP = 0.26
BOTTOM = 0.78


def write_png(path: Path, width: int, height: int, pixels: bytes, color: int) -> None:
	def chunk(typ: bytes, data: bytes) -> bytes:
		crc = zlib.crc32(typ + data) & 0xFFFFFFFF
		return struct.pack(">I", len(data)) + typ + data + struct.pack(">I", crc)

	bpp = {2: 3, 6: 4}[color]
	raw = bytearray()
	stride = width * bpp
	for y in range(height):
		raw.append(0)
		raw.extend(pixels[y * stride : (y + 1) * stride])
	ihdr = struct.pack(">IIBBBBB", width, height, 8, color, 0, 0, 0)
	png = b"\x89PNG\r\n\x1a\n"
	png += chunk(b"IHDR", ihdr)
	png += chunk(b"IDAT", zlib.compress(bytes(raw), 9))
	png += chunk(b"IEND", b"")
	path.write_bytes(png)


def barycentric(px: float, py: float, ax: float, ay: float, bx: float, by: float, cx: float, cy: float) -> bool:
	v0x, v0y = cx - ax, cy - ay
	v1x, v1y = bx - ax, by - ay
	v2x, v2y = px - ax, py - ay
	dot00 = v0x * v0x + v0y * v0y
	dot01 = v0x * v1x + v0y * v1y
	dot02 = v0x * v2x + v0y * v2y
	dot11 = v1x * v1x + v1y * v1y
	dot12 = v1x * v2x + v1y * v2y
	denom = dot00 * dot11 - dot01 * dot01
	if denom == 0:
		return False
	inv = 1 / denom
	u = (dot11 * dot02 - dot01 * dot12) * inv
	v = (dot00 * dot12 - dot01 * dot02) * inv
	return u >= 0 and v >= 0 and (u + v) <= 1


def triangles() -> list[tuple[tuple[float, float], tuple[float, float], tuple[float, float]]]:
	left_x0 = PAD
	left_x1 = 0.5 - GAP / 2
	right_x0 = 0.5 + GAP / 2
	right_x1 = 1 - PAD
	return [
		((left_x0, TOP), (left_x1, TOP), ((left_x0 + left_x1) / 2, BOTTOM)),
		((right_x0, TOP), (right_x1, TOP), ((right_x0 + right_x1) / 2, BOTTOM)),
	]


def raster_rgba(size: int, supersample: int = 8) -> bytes:
	src = size * supersample
	coverage = [0] * (src * src)
	tris = triangles()
	for y in range(src):
		py = (y + 0.5) / src
		for x in range(src):
			px = (x + 0.5) / src
			for a, b, c in tris:
				if barycentric(px, py, a[0], a[1], b[0], b[1], c[0], c[1]):
					coverage[y * src + x] = 1
					break
	out = bytearray(size * size * 4)
	r, g, b = GREY
	block = supersample * supersample
	for y in range(size):
		for x in range(size):
			s = 0
			for dy in range(supersample):
				row = (y * supersample + dy) * src + x * supersample
				s += sum(coverage[row : row + supersample])
			a = round(255 * s / block)
			i = (y * size + x) * 4
			out[i : i + 4] = bytes((r, g, b, a))
	return bytes(out)


def flatten_white(rgba: bytes, size: int) -> bytes:
	out = bytearray(size * size * 3)
	for i in range(size * size):
		r, g, b, a = rgba[i * 4 : i * 4 + 4]
		t = a / 255
		out[i * 3] = round(r * t + 255 * (1 - t))
		out[i * 3 + 1] = round(g * t + 255 * (1 - t))
		out[i * 3 + 2] = round(b * t + 255 * (1 - t))
	return bytes(out)


def main() -> None:
	pkg = ROOT / "Autoscroll"
	pub = ROOT / "publish"
	for size in (16, 48, 128):
		rgba = raster_rgba(size)
		dest = pkg / f"icon-{size}.png"
		write_png(dest, size, size, rgba, 6)
		print(f"{dest.relative_to(ROOT)}: {size}×{size} RGBA")
	rgba128 = raster_rgba(128)
	store = pub / "icon-128.png"
	write_png(store, 128, 128, flatten_white(rgba128, 128), 2)
	print(f"{store.relative_to(ROOT)}: 128×128 RGB (white)")


if __name__ == "__main__":
	sys.exit(main())
