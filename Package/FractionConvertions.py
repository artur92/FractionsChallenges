from fractions import Fraction as Frac
from Package.Messages import Messages


class FractionConversions(Messages):

    def convert_mixed_improper(self, fraction):
        """
        This methos will convert any mixed fraction (numerator bigger than denominator into a improper fraction
        (number_numerator/denominator)
        :param fraction: Mixed fraction to be convert as String
        :return: Improper fraction
                False if the fraction cant be convert
        """
        try:
            mixed_operator = '_'
            if mixed_operator in fraction:
                mixed_fraction = fraction.split(mixed_operator)
                number = int(mixed_fraction[0])
                flag = 1
                if '-' in fraction:
                    flag = -1
                fraction = Frac(mixed_fraction[1])
                if number == 0:
                    return str(fraction * flag)
                new_numerator = (abs(number) * int(fraction.denominator) + int(fraction.numerator)) * flag
                return str(Frac(new_numerator, fraction.denominator))
            return str(Frac(fraction))
        except Exception as e:
            print(self.exception_happens, e)
            return False

    @staticmethod
    def convert_improper_to_mixed_fraction(fraction):
        """
        This method will convert any improper (numerator bigger than denominator) fraction into a mixed fraction
        :param fraction: (String) Improper fraction to be convert
        :return: mixed fraction (number_numerator_denominator)
        """
        fraction = Frac(fraction)
        numerator = abs(fraction.numerator)
        denominator = abs(fraction.denominator)
        flag = 1
        if fraction < 0:
            flag = -1
        if abs(numerator) > abs(denominator):
            number = numerator // denominator
            new_fraction = Frac((numerator % denominator), denominator)
            if new_fraction != 0:
                return str(number * flag) + '_' + str(new_fraction)
            return str(number * flag)
        return fraction

    def execute_operation(self, frac1, operator, frac2):
        """
        This method is in charge of doing the fractional operation (add, subtraction, division, multiplication)
        :param frac1: first operator
        :param operator: operation to be performed
        :param frac2: second operator
        :return: the result of the operation
        """
        try:
            ops = {"+": (lambda x, y: Frac(x) + Frac(y)), "-": (lambda x, y: Frac(x) - Frac(y)), "*":
                (lambda x, y: Frac(x) * Frac(y)), "/": (lambda x, y: Frac(x) / Frac(y))}
            if operator in ops:
                return str(ops[operator](frac1, frac2))
            else:
                print(self.operator_not_Valid)
                return False
        except Exception as e:
            print(self.operator_not_Valid, e)
            return False
