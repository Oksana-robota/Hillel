import unittest
from Hillel.Hillel.HW13.HW10 import Pagination



class TestCase(unittest.TestCase):

    def setUp(self):
        self.load_file = Pagination([1,2,3,4])

    def test_iter(self):
        result = list(self.load_file)
        self.assertEqual(result, [1,2,3])

    def test_iter_2(self):
        result = list(self.load_file.next_page())
        self.assertEqual(result, [4])


if __name__ == '__main__':
    unittest.main()