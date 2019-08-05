# @author Vivek
# @version 1.0
# @since 30-07-2019

import unittest

from util.Helper import Helper


class HelperTest(unittest.TestCase):
    helper = Helper()

    def test_get_num_total_days(self):
        self.assertEqual(28, self.helper.get_num_total_days(2019, 2))
        self.assertEqual(31, self.helper.get_num_total_days(2019, 7))
        self.assertEqual(30, self.helper.get_num_total_days(2019, 11))

    def test_get_num_days_left_in_month(self):
        self.assertEqual(31, self.helper.get_num_days_left_in_month(2019, 7, 1))
        self.assertEqual(1, self.helper.get_num_days_left_in_month(2019, 7, 31))


if __name__ == '__main__':
    unittest.main()
