"""test_class_parametrization.py"""
import pytest
import unittest
from Package.FractionConvertions import FractionConversions


class TestGroup(unittest.TestCase):
    fraction_conversions = FractionConversions()

    def test_convert_mixed_improper(self):
        test_data = [{'input': '-1_4/5', 'expected': '-9/5'},
                     {'input': '0_4/5', 'expected': '4/5'}]
        for data in test_data:
            result = self.fraction_conversions.convert_mixed_improper(data['input'])
            self.assertEqual(result, data['expected'], 'The convert mixed to improper is not correct')

    def test_convert_improper_to_mixed_fraction(self):
        result = self.fraction_conversions.convert_improper_to_mixed_fraction('-10/5')
        self.assertEqual(result, '-2', 'convert_improper_to_mixed_fraction wrong result')

    def test_execute_operation_error_in_result(self):
        result = self.fraction_conversions.execute_operation('1/2', '/', '0')
        self.assertFalse(result, 'Should not be possible divide by 0')

    def test_execute_operation_no_valid_operation(self):
        result = self.fraction_conversions.execute_operation('1/2', '±', '2')
        self.assertFalse(result, '± Is not a valid operation')
