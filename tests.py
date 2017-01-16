import unittest
from format_price import format_price

class TestFormatString(unittest.TestCase):

    def test_integer_value(self):
        self.assertEqual(format_price(102343455444),'102 343 455 444','Integer value is FAIL')

    def test_float_value(self):
        self.assertEqual(format_price(102343455.444), '102 343 455.44', 'Float value is FAIL')

    def test_string_int_value(self):
        self.assertEqual(format_price("7856322152"), '7 856 322 152', 'Integer value in string is FAIL')

    def test_string_float_value(self):
        self.assertEqual(format_price("12856325.2132"), '12 856 325.21', 'Float value in string is FAIL')

    def test_string_is_not_number(self):
        with self.assertRaises(ValueError):
            format_price("blablabla")

    def test_type_value_error(self):
        with self.assertRaises(ValueError):
            format_price('234#23443!34@')

    def test_comma_value_error(self):
        with self.assertRaises(ValueError):
            format_price('256835,465465')

    def test_multi_point_value_error(self):
        with self.assertRaises(ValueError):
            format_price('452.253.635')

    def test_negative_value_error(self):
        with self.assertRaises(ValueError):
            format_price('-256835.465465')

if __name__ == '__main__':
    unittest.main()