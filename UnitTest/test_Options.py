"""test_class_parametrization.py"""
import pytest
import unittest
from Package.Options import Operations


class TestOptions(unittest.TestCase):
    operator = Operations()

    def test_input_validation_valid_data(self):
        test_data = ['1/2 + 1/4', '3_1/2 - 1/4', '1/2 - -1_1/4', '1_1/12 + 3_1/2']
        for data in test_data:
            self.assertTrue(self.operator.input_validation(data), 'Input data should be true')

    def test_input_validation_not_valid_fractions(self):
        test_data = ['1/2 + 1/b', '1/b + 1/b', '1/b + 1/b', 'a/b + a/b', 'a/2 + a/2', '1/b + 1/2', '1_1/b + 3_1/2']
        for data in test_data:
            self.assertFalse(self.operator.input_validation(data), 'Input data should be true')

    def test_input_invalid_operation(self):
        test_data = ['1/b > 1/2', '1/b L 1/2', '1/b ** 1/2']
        for data in test_data:
            self.assertFalse(self.operator.input_validation(data), 'The operations is valid')

    def test_input_missing_parameters(self):
        self.assertFalse(self.operator.input_validation('1/b  1/2'), 'There are not enough parameters to '
                                                                     'perform the operation')

    def test_more_parameters(self):
        self.assertFalse(self.operator.input_validation('1/3 + 1/2 + 1/8 *8'), 'There are more parameters than expected'
                         )

    def test_get_result_correct(self):
        test_data = [{'operand1': '1/2', 'operation': '+', 'operand2': '1/4', 'result': '3/4'},
                     {'operand1': '1/2', 'operation': '-', 'operand2': '2', 'result': '-1_1/2'},
                     {'operand1': '4/24', 'operation': '/', 'operand2': '1/7', 'result': '1_1/6'},
                     {'operand1': '11/5', 'operation': '*', 'operand2': '17/5', 'result': '7_12/25'}
                     ]
        for data in test_data:
            self.operator.set_parameters(data['operand1'], data['operation'], data['operand2'])
            self.assertEqual(str(self.operator.get_result()), data['result'], f'The result of the operation '
                                                                              f'is not correct')
