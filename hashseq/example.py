from __future__ import annotations

import argparse
import json
from typing import Any

from .core import consume_without_replacement, normalize_hash


def build_double_color_ball(
    hash_hex: str,
    red_population: int = 33,
    red_count: int = 6,
    blue_population: int = 16,
    blue_count: int = 1,
) -> dict[str, list[int]]:
    value = int(normalize_hash(hash_hex), 16)
    red, remainder = consume_without_replacement(hex(value), red_population, red_count)
    blue, _ = consume_without_replacement(hex(remainder), blue_population, blue_count)
    return {"red": red, "blue": blue}


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a deterministic 双色球-style draw from a hash")
    parser.add_argument("--hash", required=True, help="Hexadecimal blockchain hash")
    parser.add_argument("--red", type=int, default=33, help="Red ball population")
    parser.add_argument("--red-count", type=int, default=6, help="Red ball count")
    parser.add_argument("--blue", type=int, default=16, help="Blue ball population")
    parser.add_argument("--blue-count", type=int, default=1, help="Blue ball count")
    parser.add_argument("--json", action="store_true", help="Print JSON output")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    result = build_double_color_ball(
        args.hash,
        red_population=args.red,
        red_count=args.red_count,
        blue_population=args.blue,
        blue_count=args.blue_count,
    )
    if args.json:
        print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    else:
        print(f"red: {result['red']}")
        print(f"blue: {result['blue']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
