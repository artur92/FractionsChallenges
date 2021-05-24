"""test_class_parametrization.py"""
import unittest
from Package.Options import Operations


class TestGroup(unittest.TestCase):
    operator = Operations()

    def test_valid_input(self):
        test_data = [{'operation': '1/2 + 1/4', 'result': '3/4'},
                     {'operation': '5_1/23 - 8_1/4', 'result': '-3_19/92'},
                     {'operation': '5_1/23 * 23_1/4', 'result': '117_6/23'},
                     {'operation': '5_1/23 +  23_1/4', 'result': '28_27/92'},
                     {'operation': '2_4/7 /  3_1/4', 'result': '72/91'},
                     {'operation': '0_1/3 /  3_1/4', 'result': '4/39'},
                     {'operation': '0_1/3 / -8_1/4', 'result': '-4/99'},
                     {'operation': '0_1/3 / -8_0/4', 'result': '-1/24'},
                     {'operation': '0_0/3 / -8_0/4', 'result': '0'},
                     {'operation': '0_0/3 / 1/4', 'result': '0'},
                     {'operation': '-0_0/3 / 1/4', 'result': '0'},
                     {'operation': '-0_0/3 / -1/4', 'result': '0'},
                     {'operation': '0_1/3 / -8_1/4', 'result': '-4/99'},
                     {'operation': '-0_0/3 - -1/4', 'result': '1/4'},
                     {'operation': '-0_0/3 + -1/4', 'result': '-1/4'},
                     {'operation': '-10_0/3 * -1/4', 'result': '2_1/2'},
                     {'operation': '-10_0/3 / -1/4', 'result': '40'}
                     ]
        for data in test_data:
            self.assertTrue(self.operator.input_validation(data['operation']), 'The input is not valid')
            self.assertEqual(str(self.operator.get_result()), data['result'], f'The result is not correct')

    def test_operation_not_possible(self):
        test_data = ['-10_0/3 / -1/0', '-1_0_0/3 +  -1/0', '-1_0_0/3 +  -1/0' ]
        for data in test_data:
            self.assertFalse(self.operator.input_validation(data), 'Input data should be true')

    def test_wrong_data(self):
        test_data = ['1/2 +1/4', '0_1/3 / -8_o1/4', '-10_0/3 [ -1/0', '-10_0/3 . -1/0', '-10_0/3  -1/0' , ]
        for data in test_data:
            self.assertFalse(self.operator.input_validation(data), 'The operations is valid')

