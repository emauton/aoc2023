from aoc2023.day2 import (parse_round, parse_game, is_game_possible,
                          minimum_cubes)


def test_parse_round():
    '''parses a round segment into a tuple (r, g, b)'''
    assert parse_round('13 red, 18 green') == (13, 18, 0)


def test_parse_game():
    '''parses a game line into a list of tuple rounds [(r, g, b), ...]'''
    input = ('Game 1: 13 red, 18 green; 5 green, 3 red, 5 blue; '
             '5 green, 9 red, 6 blue; 3 blue, 3 green')
    expected = [(13, 18, 0), (3, 5, 5), (9, 5, 6), (0, 3, 3)]
    assert parse_game(input) == expected


def test_is_game_possible():
    '''correctly identifies possible games'''
    assert is_game_possible([(4, 3, 0), (1, 2, 6), (0, 2, 0)],
                            (12, 13, 14))
    assert not is_game_possible([(20, 8, 6), (4, 13, 5), (1, 5, 0)],
                                (12, 13, 14))


def test_minimum_cubes():
    '''counts the minimum cubes necessary to play a game'''
    assert minimum_cubes([(4, 3, 0), (1, 2, 6), (0, 2, 0)]) == (4, 3, 6)
    assert minimum_cubes([(20, 8, 6), (4, 13, 5), (1, 5, 0)]) == (20, 13, 6)
