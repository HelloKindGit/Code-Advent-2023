def read_cards_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.split(':')[-1].strip() for line in lines]

def process_cards(cards):
    card_counts = [1] * len(cards)

    for i, card in enumerate(cards):
        winning_numbers, numbers_you_have = card.split(" | ")

        winning_numbers = set(map(int, winning_numbers.split()))
        numbers_you_have = set(map(int, numbers_you_have.split()))

        matched_count = len(winning_numbers.intersection(numbers_you_have))

        #update the counts for the subsequent cards
        for j in range(1, matched_count + 1):
            card_counts[i + j] += card_counts[i]

    return card_counts

def total_scratchcards(cards):
    card_counts = process_cards(cards)
    return sum(card_counts)

file_path = 'day_4/part2/input.txt'  #'day_4/part2/test.txt'
cards = read_cards_from_file(file_path)

results = total_scratchcards(cards)
print(results)