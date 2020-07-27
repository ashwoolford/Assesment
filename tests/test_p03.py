import unittest
from p03 import *


class TestProblem03(unittest.TestCase):

    def test_01(self):
        self.assertEqual(lca(n6, n7), 3)

    def test_02(self):
        self.assertEqual(lca(n3, n7), 3)

    def test_03(self):
        self.assertEqual(lca(n1, n2), 1)

    def test_04(self):
        self.assertEqual(lca(n1, n7), 1)

    def test_05(self):
        self.assertEqual(lca(n8, n5), 2)

    def test_06(self):
        self.assertEqual(lca(n8, n8), 8)

    def test_07(self):
        self.assertEqual(lca(n3, n7), 3)

    def test_08(self):
        self.assertEqual(lca(n1, n1), 1)


if __name__ == '__main__':
    unittest.main()
