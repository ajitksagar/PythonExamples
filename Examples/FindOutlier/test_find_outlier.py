from unittest import TestCase

from find_outlier import find_outlier


class TestFind_outlier(TestCase):
    def test_find_outlier(self):
        self.assertEquals(find_outlier([2,4,5,6,8,10]),5)
        self.assertEquals(find_outlier([1,3,7,8,9,11]),8)

