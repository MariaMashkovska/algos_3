import unittest

from main import count_time


class MyTestCase(unittest.TestCase):
    def test_if_empty(self):
        artists = 10
        time = 5
        paper_amount = []
        result = count_time(artists, time, paper_amount)
        print(result)
        self.assertEqual(result, 0)

    def test_if_no_artist(self):
        artists = 0
        time = 5
        paper_amount = [1, 4, 3]
        result = count_time(artists, time, paper_amount)
        print(result)
        self.assertEqual(result, "Nobody is here to work")

    def test_if_artists_more(self):
        artists = 10
        time = 5
        paper_amount = [1, 4, 3]
        result = count_time(artists, time, paper_amount)
        print(result)
        self.assertEqual(result, 20)

    def test_if_papers_more(self):
        artists = 3
        time = 5
        paper_amount = [1, 4, 3, 5, 6]
        result = count_time(artists, time, paper_amount)
        print(result)
        self.assertEqual(result, 50)

    def test_if_equal(self):
        artists = 3
        time = 5
        paper_amount = [1, 4, 3]
        result = count_time(artists, time, paper_amount)
        print(result)
        self.assertEqual(result, 20)

if __name__ == '__main__':
    unittest.main()
