import unittest
import calc

class CalcTest(unittest.TestCase):
    def test_mul(self):
        self.assertEqual(calc.multip(2, 4), 8)


if __name__ == '__main__':
    unittest.main()
    