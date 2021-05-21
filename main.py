from Package.Options import Operations
from CommonMethods.Parser import InputParser
from Package.Messages import Messages
"""
The command to run the application is python -i 'Fraction1 Operator Fraction2' the input is expected to be pass 
as a string, each value should be separated by a blank spaces otherwise and error will be thrown.
"""

if __name__ == "__main__":
    operator = Operations()
    parser = InputParser()
    messages = Messages()
    if operator.input_validation(parser.parser_input()):
        print(operator.get_result())
    else:
        print(messages.something_wrong)
