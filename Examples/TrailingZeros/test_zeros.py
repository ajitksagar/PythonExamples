from unittest import TestCase
from TrailingZeros import *

class TestZeros(TestCase):
    def test_zeros(self):
        self.assertEquals(zeros_recursion(52),12)
        self.assertEquals(zeros_loop(52), 12)
        self.assertEquals(zeros(52), 12)
