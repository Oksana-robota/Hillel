import unittest
from Hillel.Hillel.HW13.HW10 import FileStorage


def test_load_from_file():
    assert isinstance(FileStorage.load_from_file('file.txt')[1], dict)
def test_list_of_courses():
    assert FileStorage.list_of_courses({1: [{'first_name': 1, 'last_name': 3}], 2: []})


if __name__ == '__main__':
    unittest.main()