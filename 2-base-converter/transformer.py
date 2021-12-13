import argparse


class Transformer(object):
    """Convert numbers from base 10 integers to base N strings and back again.
    Sample usage:
    >>> base20 = Transformer('0123456789abcdefghij')
    >>> base20.from_decimal(1234)
    '31e'
    >>> base20.to_decimal('31e')
    1234
    """
    decimal_digits = '0123456789'

    def __init__(self, digits):
        self.digits = digits

    def from_decimal(self, i):
        return self._convert(i, self.decimal_digits, self.digits)

    def to_decimal(self, s):
        return int(self._convert(s, self.digits, self.decimal_digits))

    def _convert(self, number, fromdigits, todigits):
        """Convert number expressed in fromdigits to base N number
           expressed in todigits"""
        from_base = len(fromdigits)
        to_base = len(todigits)

        if from_base == 10 and to_base == 10:
            if type(number) == int:
                return str(number)
            elif type(number) == str:
                return int(number)

        # number -> absolute
        # get sign and get absolute value of number
        if from_base == 10:
            assert type(number) == int, "base 10 number must be of type int"
            is_signed = number < 0
            absolute = abs(number)
        else:
            assert type(number) == str, "base N number must be of type string"
            is_signed = number[0] == '-'
            absolute = number[is_signed:]

        # absolute -> absolute_base_10
        # convert intermediate result to base 10
        if from_base == 10:
            absolute_base_10 = absolute
        else:
            multiplier = 1
            absolute_base_10 = 0
            for i in range(len(absolute) - 1, -1, -1):
                absolute_base_10 += (
                    multiplier * fromdigits.index(absolute[i]))
                multiplier *= from_base

        # absolute_base_10 -> absolute_base_n
        # convert intermediate result to destination base n
        if to_base == 10:
            absolute_base_n = absolute_base_10
        else:
            divisor = to_base
            absolute_base_n = ""
            while absolute_base_10:
                absolute_base_n += todigits[absolute_base_10 % divisor]
                absolute_base_10 //= divisor
            absolute_base_n = absolute_base_n[::-1]
            if len(absolute_base_n) == 0:
                absolute_base_n = "0"

        # absolute_base_n -> number_base_n
        # apply sign to intermediate result to get final result
        if to_base == 10:
            sign = -1 if is_signed else 1
            number_base_n = sign * absolute_base_n
        else:
            number_base_n = "-"[:is_signed]
            number_base_n += absolute_base_n

        return number_base_n


def main():
    """main function to parse keyword arguments and perform transformation"""
    description = ("Convert numbers from base 10 integers "
                   "to base N strings and back again.")
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        '--digits', required=True, type=str,
        help="Input digits for base N number to use")
    parser.add_argument(
        '--from_decimal', nargs='+', type=int, dest='number_base_10',
        help="Input base N number to convert to base 10")
    parser.add_argument(
        '--to_decimal', nargs='+', type=str, dest='number_base_N',
        help="Input base 10 number to convert to base N")
    args = parser.parse_args()
    print(args)

    transformer = Transformer(args.digits)
    result_template = (
        "Converted base {from_base} number {source_number} to "
        "base {to_base};\n{destination_number}")

    if args.number_base_10 is not None:
        for number_base_10 in args.number_base_10:
            number_base_N = transformer.from_decimal(number_base_10)
            result_message = result_template.format(
                from_base=10, source_number=number_base_10,
                to_base=len(args.digits), destination_number=number_base_N)
            print(result_message)

    if args.number_base_N is not None:
        for number_base_N in args.number_base_N:
            number_base_10 = transformer.to_decimal(number_base_N)
            result_message = result_template.format(
                from_base=len(args.digits), source_number=number_base_N,
                to_base=10, destination_number=number_base_10)
            print(result_message)


if __name__ == "__main__":
    main()
