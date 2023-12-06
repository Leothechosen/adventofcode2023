import functools

def part1(data):
    time = list(map(int, filter(lambda x: x != "", data[0].split(":")[1].strip().split(" "))))
    distance = list(map(int, filter(lambda x: x != "", data[1].split(":")[1].strip().split(" "))))
    races = zip(time, distance)
    ways_to_beat_record = []
    for time, min_distance in races:
        times_record_broken = 0
        for seconds_held in range(time):
            speed = seconds_held
            travel_time = time - seconds_held
            if speed*travel_time > min_distance:
                times_record_broken += 1
        ways_to_beat_record.append(times_record_broken)
    return functools.reduce(lambda accum, curr_val: accum*curr_val, ways_to_beat_record)


def part2(data):
    time = int(''.join(list(filter(lambda x: x != "", data[0].split(":")[1].strip().split(" ")))))
    min_distance = int(''.join(list(filter(lambda x: x != "", data[1].split(":")[1].strip().split(" ")))))
    
    for seconds_held in range(time):
        speed = seconds_held
        travel_time = time - seconds_held
        if speed*travel_time > min_distance:
            break
    start = seconds_held
    for seconds_held in range(time, -1, -1):
        speed = seconds_held
        travel_time = time - seconds_held
        if speed*travel_time > min_distance:
            break
    end = seconds_held+1
    return end-start


if __name__ == "__main__":
    with open('Day6\data.txt', 'r') as f:
        data = f.read()
    data = data.split("\n")
    #print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")

# Distance Travelled = (seconds_traveling * seconds_held)