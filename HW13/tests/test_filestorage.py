import unittest
from Hillel.Hillel.HW13.HW10 import FileStorage


class TestCase(unittest.TestCase):

    def setUp(self):
        self.load_file = FileStorage.load_from_file('file.txt')


    def test_load_from_file(self):
        assert isinstance(self.load_file[1], dict)
    def test_list_of_courses(self):
        assert FileStorage.list_of_courses({1: [{'first_name': 1, 'last_name': 3}], 2: []})


if __name__ == '__main__':
    unittest.main()