'''Advent of Code 2023 day 1: Trebuchet?!
   https://adventofcode.com/2023/day/1'''

LETTERS = {'one': '1',
           'two': '2',
           'three': '3',
           'four': '4',
           'five': '5',
           'six': '6',
           'seven': '7',
           'eight': '8',
           'nine': '9'}


NUMBERS = {value: value for value in LETTERS.values()}


def reverse_keys(dictionary):
    return {key[::-1]: value for key, value in dictionary.items()}


def get_digit(line, table):
    prefixes = [line[:i] for i in range(1, len(line) + 1)]
    for p in prefixes:
        for key, value in table.items():
            if p.endswith(key) or p.endswith(value):
                return value


def get_calibration_value(line, table):
    first = get_digit(line, table)
    last = get_digit(line[::-1], reverse_keys(table))
    return int(first + last)


def run(args):  # pragma: no cover
    filename = args[0]

    with open(filename) as f:
        lines = f.readlines()

    part1_total = sum([get_calibration_value(line, NUMBERS) for line in lines])
    print(f'part1 total: {part1_total}')

    part2_total = sum([get_calibration_value(line, LETTERS) for line in lines])
    print(f'part2 total: {part2_total}')
