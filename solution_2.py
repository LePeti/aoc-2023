import re

from input_2 import get_input

input = get_input()


# 1/1
# 1 game: 'Game 3: 6 red, 3 blue, 8 green; 6 blue, 12 green, 15 red; 3 blue, 18 green, 4 red'
# 1 round: ['6 red', '3 blue', '8 green']
# 1 pick: '6 red'
line = input[2]
id = int(re.findall("^Game (\\d){1,3}", line)[0])

game_str = line.replace(f"Game {id}: ", "")
game_str = game_str.split("; ")
game = [round.split(", ") for round in game_str]


def parse_picks(pick):
    foo = re.match("(\\d+) (red|green|blue)", pick)
    return {foo.group(2): int(foo.group(1))}


game = [list(map(parse_picks, round)) for round in game]


def evaluate_round(round):
    thresholds = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    pick = round[0]
    pick.keys
    return all([])
