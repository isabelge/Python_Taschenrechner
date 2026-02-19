import unittest
from main import addieren, subtraktion

class test_taschenrechner(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addieren(2, 3), 5)
        self.assertEqual(addieren(-1, 1), 0)
        self.assertEqual(addieren(0, 0), 0)

    def test_subtraktion(self):
        self.assertEqual(subtraktion(3, 3), 0)
        self.assertEqual(subtraktion(-1, 1), -2)
        self.assertEqual(subtraktion(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
