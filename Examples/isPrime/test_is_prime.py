from unittest import TestCase

from Examples.isPrime.isPrime import is_prime


class TestIs_prime(TestCase):
    # noinspection PyArgumentList,PyArgumentList
    def test_is_prime(self):
        # noinspection PyArgumentList
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(6))
        #self.fail()
