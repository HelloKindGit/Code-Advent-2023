from collections import defaultdict

def hand_type(hand):
    
    first_joker = hand.find('J')
    if first_joker > -1:
        return max([hand_type(hand[:first_joker] + joker_value + hand[first_joker + 1:]) for joker_value in card_order[1:]])

    cards = defaultdict(lambda: 0)
    for card in hand:
        cards[card] += 1

    match len(cards):
        case 1:
            return 6  # Five of a kind
        case 2:
            return 5 if 4 in cards.values() else 4  # Four of a kind or Two pair
        case 3:
            return 3 if 3 in cards.values() else 2  # Full house or Three of a kind
        case 4:
            return 1  # One pair
        case _:
            return 0  # High card
        
def sort_key(hand_bid):
    hand, _ = hand_bid
    return hand_type(hand), tuple(card_order.index(c) for c in hand)
        
card_order = 'J23456789TQKA'

with open('day_7/part2/input.txt', 'r') as file: # day_7/part2/test.txt
    hands_with_bid = [line.strip().split() for line in file]

hands_with_bid.sort(key=sort_key)

results = sum(rank * int(bid) for rank, (_, bid) in enumerate(hands_with_bid, start=1))

print(results)
