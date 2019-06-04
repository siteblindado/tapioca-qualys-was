# coding: utf-8

import unittest

from tapioca_qualys_was import Qualys_was


class TestTapiocaQualys_was(unittest.TestCase):

    def setUp(self):
        self.wrapper = Qualys_was()


if __name__ == '__main__':
    unittest.main()
