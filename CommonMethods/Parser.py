import argparse


class InputParser:

    @staticmethod
    def parser_input():
        """
        This method will check if the parameters need for the application are correct
        and example on how to input data in the script is main.py -i '1_4/7 *  9_1/8'
        :return: the input parameter pass as -i or --input
        """
        parser = argparse.ArgumentParser(description='Package operations')
        parser.add_argument('-i', '--input', type=str, required=True,
                            help='Fractional operation to be performed i.e 2/3 '
                                 '+ 1/4 mixed fraction are allow with the nex '
                                 'format 1_2/3 (and underscore for separate '
                                 'the whole number form the fraction)')
        args = parser.parse_args()
        return args.input
