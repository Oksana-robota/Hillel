import unittest
from Hillel.Hillel.HW13.HW10 import Pagination


result = list(Pagination([1,2,3,4]))
result2 = Pagination([1,2,3,4]).next_page()


def test_iter():
    assert list(result) == [1,2,3]
    assert list(result2) == [4]


if __name__ == '__main__':
    unittest.main()