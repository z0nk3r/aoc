def score(cards):
    scores = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    
    total = 0
    hand_score = [cards.count(card) for card in cards]
    print(f"{hand_score = }")

    if 5 in hand_score:             # 5oaK
        total = 6
    elif 4 in hand_score:           # 4oaK
        total = 5
    elif 3 in hand_score:           # 3oaK
        if 2 in hand_score:         # fullhouse
            total = 4
        else:
            total = 3
    elif hand_score.count(2) == 4:  # two pair
        total = 2
    elif 2 in hand_score:           # one pair
        total = 1
    else:                           # junk
        pass
    
    score_map = [scores.get(card, card) for card in cards]
    print(f"{score_map = }")
    return (total, score_map)

def part1(lines):
    ans1 = 0
    
    all_cards = []
    for line in lines:
        print(f"{line}")
        hand, bid = line.split(" ")
        all_cards.append((hand, int(bid)))
    
    all_cards.sort(key = lambda cards: score(cards[0]))
    
    for rank, (hand, bid) in enumerate(all_cards):
        print(f"{(hand, bid) = }")
        ans1 += ((rank + 1) * bid)
    
    print(f"1: {ans1}")

def part2(lines):
    for line in lines:
        pass

if __name__ == "__main__":
    lines = [line.replace("\n", "") for line in open(0).readlines()]

    print(f"{lines = }")
    part1(lines)
    # part2(lines)