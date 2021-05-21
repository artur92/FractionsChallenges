from Package.FractionConvertions import FractionConversions
from Package.Messages import Messages


class Operations(Messages):
    fractions_operations = FractionConversions()
    fraction1 = None
    operator = None
    fraction2 = None

    def input_validation(self, operation):
        """
        Check if the input parameter fulfill the minimum requirement: fraction1 operator fraction2,
        each of them separate by a blank space, also will convert any mixed (number_numerator/denominator) fraction to
        improper (numerator bigger than denominator) and will update their values.
        :param operation: input fraction operation to be perform
        :return: true or false if the input requisites are fulfill
        """
        input_operation = operation.split()
        if len(input_operation) != 3:
            print(self.input_not_valid)
            return False
        return self.set_parameters(input_operation[0], input_operation[1], input_operation[2])

    def get_result(self):
        """
        This method will executed the fractional operation and will convert the result into a mixed fraction
        (number_numerator/denominator)
        :return: result of the operation
        """
        result = self.fractions_operations.execute_operation(self.fraction1, self.operator, self.fraction2)
        result = self.fractions_operations.convert_improper_to_mixed_fraction(result)
        return result

    def set_parameters(self, operand1, operator, operand2):
        """
        This method will set the values for perform the operation
        :param operand1: value1 to perform the operation
        :param operator: type of operation to be done
        :param operand2: value2 to perfom the operation
        :return: true if the all the input parameters are correct, false if there was an issue with the input
        """
        self.fraction1 = self.fractions_operations.convert_mixed_improper(operand1)
        self.operator = operator
        self.fraction2 = self.fractions_operations.convert_mixed_improper(operand2)
        if self.fraction1 and self.operator and self.fraction2:
            return True
        return False
