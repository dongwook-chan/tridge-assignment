import numpy


from transformer import Transformer


digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def test_positive():
    for base in range(2, len(digits)):
        transformer = Transformer(digits[:base])
        for number in range(1, 101):
            number_base_N = numpy.base_repr(number, base)
            # decimal to base N
            assert transformer.from_decimal(number) == number_base_N
            # base N to decimal
            assert transformer.to_decimal(number_base_N) == number


def test_negative():
    for base in range(2, len(digits)):
        transformer = Transformer(digits[:base])
        for number in range(-100, 0):
            number_base_N = numpy.base_repr(number, base)
            # decimal to base N
            assert transformer.from_decimal(number) == number_base_N
            # base N to decimal
            assert transformer.to_decimal(number_base_N) == number


def test_zero():
    for base in range(2, len(digits)):
        transformer = Transformer(digits[:base])

        error_message = "0 must be converted to 0"
        # decimal to base N
        assert transformer.from_decimal(0) == "0", error_message
        # base N to decimal
        assert transformer.to_decimal("0") == 0, error_message
