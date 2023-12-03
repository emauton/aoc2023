'''Advent of Code 2023 day 2: Cube Conundrum
   https://adventofcode.com/2023/day/2'''


import re


RED = re.compile(r'(\d+) red')
GREEN = re.compile(r'(\d+) green')
BLUE = re.compile(r'(\d+) blue')


def parse_round(segment):
    r = g = b = 0
    m = RED.search(segment)
    if m:
        r = int(m.group(1))
    m = GREEN.search(segment)
    if m:
        g = int(m.group(1))
    m = BLUE.search(segment)
    if m:
        b = int(m.group(1))
    return (r, g, b)


def parse_game(line):
    '''Parse a game line into a list of tuple rounds, [(r, g, b), ...]

    Example:
    Game 1: 13 red, 18 green; 5 green, 3 red, 5 blue; 5 green, 9 red, 6 blue

    -> [(13, 18, 0), (3, 5, 5), (9, 5, 6)]'''
    return [parse_round(segment) for segment in line.split(';')]


def is_game_possible(game, cubes):
    max_r, max_g, max_b = cubes
    for (r, g, b) in game:
        if r > max_r or g > max_g or b > max_b:
            return False
    return True


def minimum_cubes(game):
    max_r = max_g = max_b = 0
    for (r, g, b) in game:
        max_r = max(r, max_r)
        max_g = max(g, max_g)
        max_b = max(b, max_b)
    return (max_r, max_g, max_b)


def run(args):  # pragma: no cover
    filename = args[0]

    with open(filename) as f:
        games = [parse_game(line) for line in f.readlines()]

    part1_cubes = (12, 13, 14)
    part1_total = 0
    part2_total = 0
    for i, game in enumerate(games):
        if is_game_possible(game, part1_cubes):
            part1_total += i + 1
        (r, g, b) = minimum_cubes(game)
        part2_total += r * g * b

    print(f'part1 total: {part1_total}')
    print(f'part2 total: {part2_total}')
