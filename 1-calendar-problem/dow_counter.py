import argparse
from typing import List
import datetime

from enumerator import DayOfWeek


class DowCounter:
    def __init__(self, century: int) -> None:
        assert century >= 1, "century must be greater than 0"
        self.century = century
        self.year_lower = (century - 1) * 100 + 1
        self.year_upper = century * 100
        self.dow_of_first_day_in_century = datetime.datetime(
            year=self.year_lower, month=1, day=1).weekday()

    @staticmethod
    def get_day_of_week(year: int, month: int, day: int) -> int:
        raise NotImplementedError

    def count_dow_of_first_day_in_month(self) -> List[int]:
        dow_counter = [0] * 7
        for year in range(self.year_lower, self.year_upper + 1):
            for month in range(1, 13):
                dow = self.get_day_of_week(year=year, month=month, day=1)
                dow_counter[dow] += 1
        return dow_counter

    def months_starting_on_sunday(self) -> int:
        dow_counter = self.count_dow_of_first_day_in_month()
        return dow_counter[DayOfWeek.SUN]


class TabularDowCounter(DowCounter):
    dow_for_century_modulo_4 = [[172, 171, 173, 169, 173, 171, 171],
                                [172, 172, 170, 173, 170, 171, 172],
                                [170, 173, 170, 171, 172, 172, 172],
                                [170, 171, 172, 172, 172, 170, 173]]

    def count_dow_of_first_day_in_month(self) -> List[int]:
        return self.dow_for_century_modulo_4[self.century % 4]


class FormulaDowCounter(DowCounter):
    dow_for_month = [-1, 6, 2, 1, 4, 6, 2, 4, 0, 3, 5, 1, 3]

    def get_day_of_week(self, year: int, month: int, day: int) -> int:
        if (month < 3):
            year -= 1

        return ((year + year // 4 - year // 100 + year // 400 +
                 self.dow_for_month[month] + day) % 7)


class BruteForceDowCounter(DowCounter):
    days_in_month = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, century: int) -> None:
        super().__init__(century)
        self.prev_dow = self.dow_of_first_day_in_century

    @staticmethod
    def _is_leap(year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def get_days_in_month(self, year: int, month: int) -> int:
        if self._is_leap(year) and month == 2:
            return 29
        return self.days_in_month[month]

    def get_day_of_week(self, year: int, month: int, day: int) -> int:
        prev_dow = dow = self.prev_dow
        dow += self.get_days_in_month(year, month)
        dow %= 7
        self.prev_dow = dow

        return prev_dow


class StdLibDowCounter(DowCounter):
    def __init__(self, century: int) -> None:
        assert century < 100, "maximum year for datetime is 9999"
        super().__init__(century)

    @staticmethod
    def get_day_of_week(year: int, month: int, day: int) -> int:
        return datetime.datetime(year=year, month=month, day=day).weekday()


counter_map = [TabularDowCounter, FormulaDowCounter, BruteForceDowCounter,
               StdLibDowCounter]


def main():
    description = "Count months starting on Sunday in the input century."
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--mode', nargs=1, default=0,
                        type=int, metavar="[0-3]", choices=range(0, 4),
                        help='Input mode to determine algorithm')
    parser.add_argument('--century', nargs=1, default=[20],
                        type=int, metavar=">=1", choices=range(0, 10000),
                        help='Input a century to inspect (default: 20)')
    args = parser.parse_args()

    dow_counter_class = counter_map[args.mode[0]]
    dow_counter = dow_counter_class(args.century[0])
    answer = dow_counter.months_starting_on_sunday()
    print((f"The number of months starting on sunday in {args.century[0]}th "
           f"century is;\n{answer}"))


if __name__ == "__main__":
    main()
