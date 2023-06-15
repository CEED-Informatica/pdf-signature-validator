import unittest

import sys
sys.path.append("./src/pdf_signature_validator")

from src.pdf_signature_validator import *

class TestSimple(unittest.TestCase):

    def test_add(self):
        # self.assertEqual((Number(5) + Number(6)).value, 11)
        self.assertEqual(1 + 2, 3)


if __name__ == '__main__':
    unittest.main()
