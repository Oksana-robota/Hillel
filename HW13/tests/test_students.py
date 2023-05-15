import unittest
from Hillel.Hillel.HW13.HW10 import Courses

class TestCase(unittest.TestCase):

    def setUp(self):
        self.list_students = Courses()


    def test_list_students(self):
        assert isinstance(self.list_students.list_for_pagination({1: [{'first_name': 1, 'last_name': 3}], 2: []}), list)

