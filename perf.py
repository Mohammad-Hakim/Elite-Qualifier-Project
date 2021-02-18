import time
import unittest
from main import ranking

class PerformanceTestRanking(unittest.TestCase):

    def test_ranking(self):
        rank = 8
        self.assertTrue(ranking(str(rank)).isdigit())

    def test_perf(self):
        start_time = time.time()
        for i in range(1):
            self.test_ranking(i)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Test took ' + str(elapsed_time) + ' seconds.')
        # test that elapsed time is less than 10 seconds
        self.assertTrue(elapsed_time < 10.0)

if __name__ == '__main__':
    unittest.main()