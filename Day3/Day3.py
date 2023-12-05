import re

def part1(data):
    ans = 0
    for line_index, line in enumerate(data):
        numbers_in_line = re.findall("[0-9]*", line)
        char_index = 0
        for number in numbers_in_line:
            if not number:
                char_index += 1
                continue
            num_len = len(number)
            text_above = ''
            text_below = ''
            text_left = ''
            text_right = ''
            if line_index != 0: 
                text_above = data[line_index-1][max(char_index-1, 0):min(char_index+num_len+1, len(line))]
            if line_index != len(data)-1:
                text_below = data[line_index+1][max(char_index-1, 0):min(char_index+num_len+1, len(line))]
            if char_index != 0:
                text_left = line[char_index-1]
            if char_index != len(line)-num_len:
                text_right = line[char_index+num_len]
            surrounding_text = text_above+text_below+text_left+text_right
            if re.search(r'[^0-9.]', surrounding_text):
                ans += int(number)
            char_index += num_len            
    return ans

def part2(data):
    #Example Data ans: 467835
    #Real Data ans: 79613331
    pass


if __name__ == "__main__":
    with open('Day3\data.txt', 'r') as f:
        data = f.read()
    #part2someoneelse()
    data = data.split("\n")
    print(f"Part 1: {part1(data)}")
    #print(f"Part 2: {part2(data)}")

