from typing import List

from dow_counter import DowCounter, StdLibDowCounter


error_template = ("incorrect solution of {class_name} for "
                  "{century}th century: {solution}\n"
                  "correct answer: {answer}\n")


def counters_to_test(
        century: int, counter_to_ignore: List[str] = []) -> List[object]:
    counter_to_ignore.append('StdLibDowCounter')
    instances = []

    for subclass in DowCounter.__subclasses__():
        if subclass.__name__ in counter_to_ignore:
            continue
        instance = subclass(century)
        instances.append(instance)

    return instances


def test_by_month() -> None:
    year_lower = 1
    year_upper = 9999
    century_lower = year_lower // 100 + 1

    accurate_counter = StdLibDowCounter(century_lower)

    for counter in counters_to_test(
            century_lower, counter_to_ignore=['TabularDowCounter']):
        for year in range(year_lower, year_upper + 1):
            century = year // 100 + 1
            for month in range(1, 13):
                answer = accurate_counter.get_day_of_week(
                    year=year, month=month, day=1)
                solution = counter.get_day_of_week(
                    year=year, month=month, day=1)

                error_template = (
                    "incorrect solution of {class_name} for "
                    "{century}th century {year}th year {month}th month"
                    ": {solution}\ncorrect answer: {answer}\n")

                error_message = error_template.format(
                    class_name=counter.__class__.__name__, century=century,
                    year=year, month=month, solution=solution, answer=answer)

                assert answer == solution, error_message


def test_by_century() -> None:
    for century in range(1, 100):
        accurate_counter = StdLibDowCounter(century)
        answer = accurate_counter.count_dow_of_first_day_in_month()

        for counter in counters_to_test(century):
            solution = counter.count_dow_of_first_day_in_month()

            error_template = (
                "incorrect solution of {class_name} for "
                "{century}th century: {solution}\n"
                "correct answer: {answer}\n")

            error_message = error_template.format(
                class_name=counter.__class__.__name__, century=century,
                solution=solution, answer=answer)

            assert answer == solution, error_message
