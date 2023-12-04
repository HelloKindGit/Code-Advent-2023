def read_cards_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.split(':')[-1].strip() for line in lines]

def calculate_points(card):
    winning_numbers, numbers_you_have = card.split(" | ")
    
    winning_numbers = set(map(int, winning_numbers.split()))
    numbers_you_have = set(map(int, numbers_you_have.split()))

    matches = len(winning_numbers.intersection(numbers_you_have))

    points = 2 ** (matches - 1) if matches > 0 else 0

    return points

def total_points(cards):
    return sum(calculate_points(card) for card in cards)

file_path = 'day_4/part1/input.txt' #'day_4/part1/test.txt'
cards = read_cards_from_file(file_path)

results = total_points(cards)
print(results)
