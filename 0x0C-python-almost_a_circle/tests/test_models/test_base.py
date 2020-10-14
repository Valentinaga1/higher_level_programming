#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8


class TestingBaseClass(unittest.TestCase):

    def test_pep8(self):
        """Test for PEP-8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base.py"])
        self.assertEqual(result.total_errors, 0)

    def test_id(self):
        b1 =  Base()
        self.assertEqual(b1.id, 1)

        b2 =  Base()
        self.assertEqual(b2.id, 2)

        b3 =  Base()
        self.assertEqual(b3.id, 3)

        b4 =  Base(12)
        self.assertEqual(b4.id, 12)

if __name__ == '__main__':
    unittest.main()