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

def min_count_in_round(round_data, color):
    counts = [count for count, round_color in round_data if round_color == color]
    return max(counts) if counts else 0

def min_set_power(game, red_count, green_count, blue_count):
    min_red = min_count_in_round(game[0], 'red')
    min_green = min_count_in_round(game[0], 'green')
    min_blue = min_count_in_round(game[0], 'blue')
    
    return min_red * min_green * min_blue

def total_power_sum(file_path, red_count, green_count, blue_count):
    games = parse_input(file_path)
    total_power = sum(min_set_power(game[1], red_count, green_count, blue_count) for game in games)
    return total_power

file_path = 'day_2/part2/input.txt' #'day_2/part2/test.txt'
red_cubes = 12
green_cubes = 13
blue_cubes = 14
result = total_power_sum(file_path, red_cubes, green_cubes, blue_cubes)
print(result)
