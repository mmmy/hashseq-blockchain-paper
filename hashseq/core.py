from __future__ import annotations

from typing import Tuple

_HEX_DIGITS = frozenset("0123456789abcdef")


def normalize_hash(hash_hex: str) -> str:
    cleaned = hash_hex.strip().lower()
    if cleaned.startswith("0x"):
        cleaned = cleaned[2:]
    if not cleaned:
        raise ValueError("hash_hex must not be empty")
    if any(char not in _HEX_DIGITS for char in cleaned):
        raise ValueError("hash_hex must contain only hexadecimal characters")
    return cleaned


def _validate_base_and_count(base: int, count: int) -> None:
    if base < 1:
        raise ValueError("base must be at least 1")
    if count < 1:
        raise ValueError("count must be at least 1")


def _to_int(hash_hex: str) -> int:
    return int(normalize_hash(hash_hex), 16)


def _consume_with_replacement(value: int, base: int, count: int) -> tuple[list[int], int]:
    _validate_base_and_count(base, count)
    digits: list[int] = []
    for _ in range(count):
        digits.append((value % base) + 1)
        value //= base
    return digits, value


def _consume_without_replacement(value: int, base: int, count: int) -> tuple[list[int], int]:
    _validate_base_and_count(base, count)
    if count > base:
        raise ValueError("count cannot exceed base when sampling without replacement")

    pool = list(range(1, base + 1))
    digits: list[int] = []
    for _ in range(count):
        size = len(pool)
        index = value % size
        digits.append(pool.pop(index))
        value //= size
    return digits, value


def draw_with_replacement(hash_hex: str, base: int, count: int) -> list[int]:
    return _consume_with_replacement(_to_int(hash_hex), base, count)[0]


def draw_without_replacement(hash_hex: str, base: int, count: int) -> list[int]:
    return _consume_without_replacement(_to_int(hash_hex), base, count)[0]


def consume_with_replacement(hash_hex: str, base: int, count: int) -> tuple[list[int], int]:
    return _consume_with_replacement(_to_int(hash_hex), base, count)


def consume_without_replacement(hash_hex: str, base: int, count: int) -> tuple[list[int], int]:
    return _consume_without_replacement(_to_int(hash_hex), base, count)

