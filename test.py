from main import ranking
import unittest

class TestStringMethods(unittest.TestCase):

    def test_ranking(self):
        self.assertTrue(ranking.isDigit())


if __name__ == '__main__':
    unittest.main()