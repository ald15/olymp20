##
# @file
# @brief    Тесты
# @author   Danya0x07
#

import unittest

from common import is_prime


class TestEverything(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(100))


if __name__ == '__main__':
    unittest.main()
