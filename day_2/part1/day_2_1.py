import re

def parse_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    games = []
    for line in lines:
        match = re.match(r"Game (\d+): (.+)$", line)
        if match:
            game_id = int(match.group(1))
            rounds = []
            round_matches = re.findall(r'(\d+) (\w+)', match.group(2))
            subset = [(int(count), color) for count, color in round_matches]
            rounds.append(subset)
            games.append((game_id, rounds))

    return games

def is_possible(game, red_count, green_count, blue_count):
    for round in game:
        for count, color in round:
            if color == 'red' and count > red_count:
                return False
            elif color == 'green' and count > green_count:
                return False
            elif color == 'blue' and count > blue_count:
                return False
    return True

def possible_games_sum(file_path, red_count, green_count, blue_count):
    games = parse_input(file_path)
    possible_sum = sum(game[0] for game in games if is_possible(game[1], red_count, green_count, blue_count))
    return possible_sum

file_path = 'day_2/part1/input.txt' #'day_2/part1/test.txt'
red_cubes = 12
green_cubes = 13
blue_cubes = 14
result = possible_games_sum(file_path, red_cubes, green_cubes, blue_cubes)
print(result)
