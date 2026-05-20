import unittest

from hashseq.core import draw_with_replacement, draw_without_replacement, normalize_hash


class CoreTests(unittest.TestCase):
    def test_normalize_hash_strips_prefix_and_whitespace(self) -> None:
        self.assertEqual(normalize_hash("  0x0F  "), "0f")

    def test_draw_with_replacement_is_stable(self) -> None:
        self.assertEqual(draw_with_replacement("0f", 16, 2), [16, 1])

    def test_draw_without_replacement_is_stable(self) -> None:
        self.assertEqual(draw_without_replacement("0f", 16, 2), [16, 1])


if __name__ == "__main__":
    unittest.main()

