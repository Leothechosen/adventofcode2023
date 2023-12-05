# https://adventofcode.com/2023/day/1

def part1(data):
    total = 0
    for line in data:
        first_num = 0
        last_num = 0
        for char in line:
            try:
                first_num = int(char)
                break
            except:
                continue
        for char in line[::-1]:
            try:
                last_num = int(char)
                break
            except:
                continue
        value = int(str(first_num) + str(last_num))
        total += value
    print(total)

def part1alt(data):
    def num_search(line):
        valid_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for char in line:
            if char in valid_numbers:
                return char
    total = 0
    for line in data:
        first_num = num_search(line)
        last_num = num_search(line[::-1])
        concat_num = first_num + last_num
        total += int(concat_num)
    print(total)
        
def part2(data):
    def num_search(line, reversed):
        valid_text_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        if reversed:
            valid_text_numbers = [text_num[::-1] for text_num in valid_text_numbers]
        valid_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        digit_num = ""
        txt_num = ""
        digit_idx = 0
        txt_num_idx = 10000000
        for i, char in enumerate(line):
            if char in valid_numbers:
                digit_idx = i
                digit_num = char
                break

        for num in valid_text_numbers:
            try:
                if num in line and line.index(num) < txt_num_idx:
                    txt_num_idx = line.index(num)
                    txt_num = str(valid_text_numbers.index(num)+1)
            except:
                continue

        if txt_num_idx < digit_idx:
            return txt_num
        else:
            return digit_num

    total = 0 
    for line in data:
        first_num = num_search(line, False)
        last_num = num_search(line[::-1], True)
        concat_num = int(first_num+last_num)
        print(line)
        print(f"{first_num=}")
        print(f"{last_num=}")
        total += concat_num
    print(total)

if __name__ == "__main__":
    with open('Day1\data.txt', 'r') as f:
        data = f.read()
    data = data.split("\n")
    #part1alt(data)
    part2(data)
    