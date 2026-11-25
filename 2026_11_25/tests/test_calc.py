import unittest

from calc import divide


class TestDivide(unittest.TestCase):
    """divide 函式的單元測試。"""

    def test_divide_normal(self) -> None:
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(-9, 3), -3.0)
        self.assertAlmostEqual(divide(7.5, 2.5), 3.0)
        self.assertEqual(divide(0, 5), 0.0)

    def test_divide_by_zero(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            divide(10, 0)
        self.assertEqual(str(ctx.exception), "除數不可為零")

    def test_divide_by_zero_float(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            divide(10, 0.0)
        self.assertEqual(str(ctx.exception), "除數不可為零")


if __name__ == "__main__":
    unittest.main()
