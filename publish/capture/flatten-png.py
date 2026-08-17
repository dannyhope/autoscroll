#!/usr/bin/env python3
"""Write a 24-bit RGB PNG (no alpha) from a Chrome screenshot or RGBA source."""
from __future__ import annotations

import struct
import sys
import zlib
from pathlib import Path


def paeth(a: int, b: int, c: int) -> int:
	p = a + b - c
	pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
	if pa <= pb and pa <= pc:
		return a
	if pb <= pc:
		return b
	return c


def read_chunks(data: bytes) -> list[tuple[bytes, bytes]]:
	assert data[:8] == b"\x89PNG\r\n\x1a\n", "not a PNG"
	off = 8
	chunks: list[tuple[bytes, bytes]] = []
	while off + 12 <= len(data):
		length = int.from_bytes(data[off : off + 4], "big")
		typ = data[off + 4 : off + 8]
		chunk = data[off + 8 : off + 8 + length]
		chunks.append((typ, chunk))
		off += 12 + length
		if typ == b"IEND":
			break
	return chunks


def decode_png(path: Path) -> tuple[int, int, bytes, int]:
	chunks = read_chunks(path.read_bytes())
	ihdr = next(c for t, c in chunks if t == b"IHDR")
	width, height, bit, color, _comp, _filt, inter = struct.unpack(">IIBBBBB", ihdr)
	if bit != 8 or inter != 0:
		raise SystemExit(f"{path}: need 8-bit non-interlaced PNG")
	raw = zlib.decompress(b"".join(c for t, c in chunks if t == b"IDAT"))
	bpp = {2: 3, 6: 4}[color]
	stride = width * bpp
	rows: list[bytes] = []
	i = 0
	prev = bytes(stride)
	for _y in range(height):
		ft = raw[i]
		i += 1
		filt = raw[i : i + stride]
		i += stride
		out = bytearray(stride)
		for x in range(stride):
			left = out[x - bpp] if x >= bpp else 0
			up = prev[x]
			ul = prev[x - bpp] if x >= bpp else 0
			v = filt[x]
			if ft == 0:
				out[x] = v
			elif ft == 1:
				out[x] = (v + left) & 255
			elif ft == 2:
				out[x] = (v + up) & 255
			elif ft == 3:
				out[x] = (v + (left + up) // 2) & 255
			elif ft == 4:
				out[x] = (v + paeth(left, up, ul)) & 255
			else:
				raise SystemExit(f"filter {ft}")
		rows.append(bytes(out))
		prev = bytes(out)
	return width, height, b"".join(rows), color


def write_png_rgb(path: Path, width: int, height: int, rgb: bytes) -> None:
	def chunk(typ: bytes, data: bytes) -> bytes:
		crc = zlib.crc32(typ + data) & 0xFFFFFFFF
		return struct.pack(">I", len(data)) + typ + data + struct.pack(">I", crc)

	raw = bytearray()
	stride = width * 3
	for y in range(height):
		raw.append(0)
		raw.extend(rgb[y * stride : (y + 1) * stride])
	ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
	png = b"\x89PNG\r\n\x1a\n"
	png += chunk(b"IHDR", ihdr)
	png += chunk(b"IDAT", zlib.compress(bytes(raw), 9))
	png += chunk(b"IEND", b"")
	path.write_bytes(png)


def flatten(src: Path, dest: Path, bg: tuple[int, int, int] = (0, 0, 0)) -> None:
	width, height, pixels, color = decode_png(src)
	out = bytearray(width * height * 3)
	if color == 2:
		out[:] = pixels
	else:
		br, bgc, bb = bg
		for i in range(width * height):
			r, g, b, a = pixels[i * 4 : i * 4 + 4]
			if a == 255:
				out[i * 3 : i * 3 + 3] = bytes((r, g, b))
			elif a == 0:
				out[i * 3 : i * 3 + 3] = bytes((br, bgc, bb))
			else:
				t = a / 255
				out[i * 3] = round(r * t + br * (1 - t))
				out[i * 3 + 1] = round(g * t + bgc * (1 - t))
				out[i * 3 + 2] = round(b * t + bb * (1 - t))
	write_png_rgb(dest, width, height, bytes(out))
	print(f"{dest.name}: {width}×{height} RGB")


if __name__ == "__main__":
	flatten(Path(sys.argv[1]), Path(sys.argv[2]))
