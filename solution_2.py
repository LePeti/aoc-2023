import operator
import re
from functools import reduce

from input_2 import get_input

# 1/1
# 1 game: 'Game 3: 6 red, 3 blue, 8 green; 6 blue, 12 green, 15 red; 3 blue, 18 green, 4 red'
# 1 round: ['6 red', '3 blue', '8 green']
# 1 pick: '6 red'


def parse_game(game_str):
    id = int(re.findall("^Game (\\d+):", game_str)[0])
    game_wo_id = line.replace(f"Game {id}: ", "")
    game_wo_id = game_wo_id.split("; ")
    return {id: [parse_round(round) for round in game_wo_id]}


def parse_round(round):
    picks = re.findall("(\\d+) (red|green|blue)", round)
    return {color: int(count) for count, color in picks}


def evaluate_round(round):
    thresholds = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    passed_evaluation = []
    for color in round.keys():
        passed_evaluation.append(round.get(color) <= thresholds.get(color))
    # print(f"{round} --> {passed_evaluation}")
    return all(passed_evaluation)


def select_max_per_color(game):
    max_per_color = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for round in game:
        for color, count_ in round.items():
            if count_ > max_per_color[color]:
                max_per_color[color] = count_
    return max_per_color


if __name__ == "__main__":
    input = get_input()

    games = {}

    for line in input:
        games.update(parse_game(line))

    games_evaluated = {}

    for id, game in games.items():
        games_evaluated[id] = True
        for round in game:
            if evaluate_round(round) is True:
                pass
            else:
                games_evaluated[id] = False
                break

    true_keys = [key for key, value in games_evaluated.items() if value]
    print(f"solution for 1/1 is: {sum(true_keys)}")

    all_games_max_per_color = [select_max_per_color(game) for game in games.values()]
    all_games_power = [
        reduce(operator.mul, color_count.values())
        for color_count in all_games_max_per_color
    ]
    print(f"solution for 1/2 is: {sum(all_games_power)}")
