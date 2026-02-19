import unittest
from main import addieren

class test_taschenrechner(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addieren(2, 3), 5)
        self.assertEqual(addieren(-1, 1), 0)
        self.assertEqual(addieren(0, 0), 0)


if __name__ == '__main__':
    unittest.main()
