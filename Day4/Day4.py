def part1(data):
    ans = 0
    for card_num, card in enumerate(data, start=1):
        wins = 0
        winning_numbers, scratched_numbers = card.split(": ")[1].split(" | ")
        winning_numbers = winning_numbers.split(" ")
        scratched_numbers = scratched_numbers.split(" ")
        for num in scratched_numbers:
            if num and num in winning_numbers:
                wins += 1
        if wins > 0:
            ans += 2**(wins-1)
    return ans

def part2(data):
    cards = {}
    for i in range(1, len(data)+1):
        cards[i] = {'count': 1}
    for card_num, card in enumerate(data, start=1):
        wins = 0
        winning_numbers, scratched_numbers = card.split(": ")[1].split(" | ")
        winning_numbers = winning_numbers.split(" ")
        scratched_numbers = scratched_numbers.split(" ")
        for num in scratched_numbers:
            if num and num in winning_numbers:
                wins += 1
        for i in range(1, wins+1):
            cards[card_num+i]['count'] += cards[card_num]['count']
    return sum([cards[card]['count'] for card in cards])


if __name__ == "__main__":
    with open('Day4\data.txt', 'r') as f:
        data = f.read()
    data = data.split("\n")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")