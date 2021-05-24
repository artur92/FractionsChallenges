import os
from CommonMethods.Parser import InputParser

command = ''
unit_test_html_report = 'pytest UnitTest/ -v --cov=Package --cov-report=html'
unit_test_cli_coverage_report = 'pytest UnitTest/ -v --cov=Package'
integration_test = 'pytest Integration/ -v'
input_value = InputParser().parser_input()
open_html = False

if input_value == 'unit_html':
    command = unit_test_html_report
    open_html = True

elif input_value == 'unit_cli':
    command = unit_test_cli_coverage_report

elif input_value == 'integration':
    command = integration_test

else:
    command = f'python3 main.py -i "{input_value}"'

os.system(command)
if open_html:
    # Check if this is valid in a windows device
    os.system('open htmlcov/index.html')
