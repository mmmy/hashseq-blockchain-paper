import unittest

from hashseq.example import build_double_color_ball


class ExampleTests(unittest.TestCase):
    def test_double_color_ball_shape(self) -> None:
        result = build_double_color_ball("0000000000000000000f")
        self.assertEqual(len(result["red"]), 6)
        self.assertEqual(len(result["blue"]), 1)


if __name__ == "__main__":
    unittest.main()

