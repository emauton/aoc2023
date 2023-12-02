from aoc2023.day1 import (reverse_keys, get_digit, get_calibration_value,
                          NUMBERS, LETTERS)


def test_reverse_keys():
    '''reverses the keys in a dictionary'''
    assert {'cba': 1, 'fed': 2} == reverse_keys({'abc': 1, 'def': 2})


def test_get_digit():
    '''gets the first digit - string or number - from a string'''
    assert get_digit('pqr3stu8vwx', NUMBERS) == '3'
    assert get_digit('xtwone3four', NUMBERS) == '3'
    assert get_digit('xtwone3four', LETTERS) == '2'


def test_get_calibration_value():
    '''returns the correct calibration value'''
    assert get_calibration_value('pqr3stu8vwx', NUMBERS) == 38
    assert get_calibration_value('xtwone3four', LETTERS) == 24
