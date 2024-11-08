def score(cards):
    scores = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    
    total = 0
    card_count = [cards.count(card) for card in cards]
    # print(f"{card_count = }")

    if 5 in card_count:             # 5oaK
        total = 6
    elif 4 in card_count:           # 4oaK
        total = 5
    elif 3 in card_count:           # 3oaK
        if 2 in card_count:         # fullhouse
            total = 4
        else:
            total = 3
    elif card_count.count(2) == 4:  # two pair
        total = 2
    elif 2 in card_count:           # one pair
        total = 1
    else:                           # junk
        pass
    
    score_map = [scores.get(card, card) for card in cards]
    # print(f"{score_map = }")
    return (total, score_map)

def score2(cards):
    scores = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    
    total = 0
    print(f"{'-'*50}\n{cards = }")
    card_count = [cards.count(card) for card in cards]
    print(f"1{card_count = }")

    highscore = 0
    highcard = sorted(cards, key = cards.count, reverse=True)[0]
    print(f"{highcard = }")
    # and scores[cards[idx]] > scores[highcard] 
    # highcard = cards[idx]
    for idx, score in enumerate(card_count):
        if cards[idx] != "J" and card_count[idx] > highscore:
            highscore = card_count[idx]

    num_jokers = cards.count("J")
    
    for idx, score in enumerate(card_count):
        if "J" in cards and score == highscore and cards[idx] == highcard:
            print(f"Count for {cards[idx]} updated cause J")
            card_count[idx] += num_jokers
    print(f"2{card_count = }")

    if 5 in card_count:             # 5oaK
        total = 6  # 5oak
    elif 4 in card_count:           # 4oaK
        total = 5  # 4oak
    elif 3 in card_count:           # 3oaK
        if 2 in card_count:         # fullhouse
            total = 4 # FH
        else:
            total = 3 # 3oaK
    elif card_count.count(2) == 4:  # two pair
        total = 2  # 2p
    elif 2 in card_count:           # one pair
        total = 1  # 1p
    else:                           # junk
        pass
    
        
    
    score_map = [scores.get(card, card) for card in cards]
    print(f"{total = }")
    print(f"{'7' > 'A' = }")
    # if cards == "AJA77":
    #     quit()
    return (total, score_map)

def part1(lines):
    ans1 = 0
    
    all_cards = []
    for line in lines:
        hand, bid = line.split(" ")
        all_cards.append((hand, int(bid)))
    
    all_cards.sort(key = lambda cards: score(cards[0]))
    
    for rank, (hand, bid) in enumerate(all_cards):
        # print(f"{(hand, bid) = }")
        ans1 += ((rank + 1) * bid)
    
    print(f"1: {ans1}")

def part2(lines):
    ans2 = 0
    
    all_cards = []
    for line in lines:
        hand, bid = line.split(" ")
        all_cards.append((hand, int(bid)))
    
    all_cards.sort(key = lambda cards: score2(cards[0]))
    
    for rank, (hand, bid) in enumerate(all_cards):
        print(f"{rank+1}: {(hand, bid)}")
        ans2 += ((rank + 1) * bid)
    
    print(f"2: 248317470 is too low")
    print(f"2: {ans2}")
    print(f"2: 249138943 is just right")
    print(f"2: 249267327 is too high")
    print(f"2: 249654276 is too high")

if __name__ == "__main__":
    lines = [line.replace("\n", "") for line in open(0).readlines()]

    # print(f"{lines = }")
    part1(lines)
    part2(lines)