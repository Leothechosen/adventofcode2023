def part1(data):
    def sort_hands(cards):
        card_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        return sorted(cards, key=lambda x: [card_order.index(card) for card in x[0]])

    ans = 0
    all_cards = {
        "five": [],
        "four": [],
        "full": [],
        "three": [],
        "two pair": [],
        "one pair": [],
        "high": []
    }
    max_rank = len(data)
    for hand in data:
        card_count = {}
        cards, bet = hand.split(" ")
        for card in cards:
            if card not in card_count:
                card_count[card] = 0
            card_count[card] += 1
        card_count = sorted(card_count.values(), reverse=True)
        if len(card_count) == 1:
            card_type = "five"
        elif len(card_count) == 2 and card_count == [4, 1]:
            card_type = "four"
        elif len(card_count) == 2 and card_count == [3, 2]:
            card_type = "full"
        elif len(card_count) == 3 and card_count == [3, 1, 1]:
            card_type = "three"
        elif len(card_count) == 3 and card_count == [2, 2, 1]:
            card_type = "two pair"
        elif len(card_count) == 4:
            card_type = "one pair"
        elif len(card_count) == 5:
            card_type = "high"
        all_cards[card_type].append((cards, int(bet)))
    for hands in all_cards.values():
        if not hands:
            continue
        if len(hands) > 1:
            hands = sort_hands(hands)
            for cards, bet in hands:
                ans += (bet * max_rank)
                max_rank -= 1
        else:
            cards, bet = hands[0]
            ans += (bet * max_rank)
            max_rank -= 1
    return ans
               
def part2(data):
    def sort_hands(cards):
        card_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
        return sorted(cards, key=lambda x: [card_order.index(card) for card in x[0]])
    ans = 0
    all_cards = {
        "five": [],
        "four": [],
        "full": [],
        "three": [],
        "two pair": [],
        "one pair": [],
        "high": []
    }
    max_rank = len(data)
    for hand in data:
        card_count = {}
        joker_count = 0
        cards, bet = hand.split(" ")
        for card in cards:
            if card == "J":
                joker_count += 1
                continue
            if card not in card_count:
                card_count[card] = 0
            card_count[card] += 1
        card_count = sorted(card_count.values(), reverse=True)
        if joker_count == 5 or joker_count == 4:
            card_type = "five"
        elif joker_count == 3 and card_count[0] == 2:
            card_type = "five"
        elif joker_count == 3 and card_count[0] == 1:
            card_type = "four"
        elif joker_count == 2 and card_count[0] == 3: 
            card_type = "five"
        elif joker_count == 2 and card_count[0] == 2: 
            card_type = "four"
        elif joker_count == 2 and card_count[0] == 1: 
            card_type = "three"
        elif joker_count == 1 and card_count[0] == 4: 
            card_type = "five"
        elif joker_count == 1 and card_count[0] == 3:
            card_type = "four"
        elif joker_count == 1 and card_count[0:2] == [2, 2]: 
            card_type = "full"
        elif joker_count == 1 and card_count[0] == 2:
            card_type = "three"
        elif joker_count == 1 and card_count[0] == 2:
            card_type = "one pair"
        else:
            if len(card_count) == 1:
                card_type = "five"
            elif len(card_count) == 2 and card_count == [4, 1]:
                card_type = "four"
            elif len(card_count) == 2 and card_count == [3, 2]:
                card_type = "full"
            elif len(card_count) == 3 and card_count == [3, 1, 1]:
                card_type = "three"
            elif len(card_count) == 3 and card_count == [2, 2, 1]:
                card_type = "two pair"
            elif len(card_count) == 4:
                card_type = "one pair"
            elif len(card_count) == 5:
                card_type = "high"
        all_cards[card_type].append((cards, int(bet)))
    for hands in all_cards.values():
        if not hands:
            continue
        if len(hands) > 1:
            hands = sort_hands(hands)
            for cards, bet in hands:
                ans += (bet * max_rank)
                max_rank -= 1
        else:
            cards, bet = hands[0]
            ans += (bet * max_rank)
            max_rank -= 1
    return ans

if __name__ == "__main__":
    with open('Day7\data.txt', 'r') as f:
        data = f.read()
    data = data.split("\n")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")