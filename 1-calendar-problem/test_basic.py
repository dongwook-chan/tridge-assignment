from dow_counter import DowCounter, StdLibDowCounter


def test_answer() -> None:
    for century in range(1, 100):
        std_lib_dow_counter = StdLibDowCounter(century)
        answer = std_lib_dow_counter.count_dow_of_first_day_in_month()

        for subclass in DowCounter.__subclasses__():
            if subclass.__name__ == 'StdLibDowCounter':
                continue
            instance = subclass(century)
            solution = instance.count_dow_of_first_day_in_month()

            err = (f"incorrect solution of {subclass.__name__} for "
                   f"{century}th century: {solution}\n"
                   f"correct answer: {answer}\n")

            assert answer == solution, err
