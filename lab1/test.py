import unittest

from lab1.algo_lab1 import return_indexes_for_target


class TestReturnIndexesForTarget(unittest.TestCase):
    def test_return_indexes_for_target(self):
        nums = [1, 9, 5, 6, 8, 4]
        target = 9
        result = return_indexes_for_target(nums, target)

        self.assertEqual(result, [[0, 4], [2, 5]])

    def test_return_indexes_for_target_no_result(self):
        nums = [1, 2, 3, 4, 5]
        target = 20
        result = return_indexes_for_target(nums, target)
        if not result:
            return -1

        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
