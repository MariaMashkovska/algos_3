import unittest

from lab1.algo_lab1 import check_if_mono


class TestReturnIndexesForTarget(unittest.TestCase):
    def test_check_if_up(self):
        nums = [1, 2, 3, 4, 5]
        result = check_if_mono(nums)

        self.assertEqual(result, True)

    def test_check_if_down(self):
        nums = [5, 4, 3, 2, 1]
        result = check_if_mono(nums)

        self.assertEqual(result, True)

    def test_check_if_mixed(self):
        nums = [5, 4, 9, 2, 5]
        result = check_if_mono(nums)

        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
