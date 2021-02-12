from main import ranking
import unittest

class TestMethods(unittest.TestCase):

    def test_ranking(self):
        rank = 8
        self.assertTrue(ranking(str(rank)).isdigit())


if __name__ == '__main__':
    unittest.main()