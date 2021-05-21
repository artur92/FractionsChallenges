from Package.Options import Operations


class CommonMethods:
    operator = Operations()

    def execute_srcipt(self, value):
        if self.operator.input_validation(parser.parser_input()):
            self.operator.get_result()
        return False
