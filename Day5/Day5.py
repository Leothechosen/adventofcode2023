import copy

def part1(data):
    def x_to_y_sorter(step, number):
        #print(f"{number}")
        #print(f"{number} -> ", end='')
        for line in step:
            dest_start, source_start, range_len = map(int, line.split(" "))
            if number in range(source_start, source_start+range_len):
                return dest_start + (number-source_start)
        return number

    seeds = data.split("seeds: ")[1].split("\n\n")[0].split(" ")
    seed_to_soil = data.split("seed-to-soil map:\n")[1].split("\n\n")[0].split("\n")
    soil_to_fert = data.split("soil-to-fertilizer map:\n")[1].split("\n\n")[0].split("\n")
    fert_to_water = data.split("fertilizer-to-water map:\n")[1].split("\n\n")[0].split("\n")
    water_to_light = data.split("water-to-light map:\n")[1].split("\n\n")[0].split("\n")
    light_to_temp = data.split("light-to-temperature map:\n")[1].split("\n\n")[0].split("\n")
    temp_to_humid = data.split("temperature-to-humidity map:\n")[1].split("\n\n")[0].split("\n")
    humid_to_location = data.split("humidity-to-location map:\n")[1].split("\n\n")[0].split("\n")
    locations = []
    for seed in map(int, seeds):
        for func in [seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_humid, humid_to_location]:
            seed = x_to_y_sorter(func, seed)
        #print(f"{seed}")
        locations.append(seed)
    return min(locations)  
                                

def part2(data):
    def x_to_y_sorter(step, number):
        #print(f"{number}")
        #print(f"{number} -> ", end='')
        for line in step:
            dest_start, source_start, range_len = map(int, line.split(" "))
            if number in range(source_start, source_start+range_len):
                return dest_start + (number-source_start)
        return number

    seeds = data.split("seeds: ")[1].split("\n\n")[0].split(" ")
    seed_to_soil = data.split("seed-to-soil map:\n")[1].split("\n\n")[0].split("\n")
    soil_to_fert = data.split("soil-to-fertilizer map:\n")[1].split("\n\n")[0].split("\n")
    fert_to_water = data.split("fertilizer-to-water map:\n")[1].split("\n\n")[0].split("\n")
    water_to_light = data.split("water-to-light map:\n")[1].split("\n\n")[0].split("\n")
    light_to_temp = data.split("light-to-temperature map:\n")[1].split("\n\n")[0].split("\n")
    temp_to_humid = data.split("temperature-to-humidity map:\n")[1].split("\n\n")[0].split("\n")
    humid_to_location = data.split("humidity-to-location map:\n")[1].split("\n\n")[0].split("\n")
    locations = []
    seed_pairs = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
    for i, (seed_start, seed_len) in enumerate(seed_pairs, start=1):
        print(f"Starting {i} seed pair of {len(seed_pairs)}")
        for seed in range(int(seed_start), int(seed_start)+int(seed_len)):
            for func in [seed_to_soil, soil_to_fert, fert_to_water, water_to_light, light_to_temp, temp_to_humid, humid_to_location]:
                seed = x_to_y_sorter(func, seed)
            #print(f"{seed}")
            locations.append(seed)
    return min(locations)

def part2reverse(data):
    def y_to_x(step, number):
        #print(f"{number}")
        #print(f"{number} -> ", end='')
        for line in step:
            dest_start, source_start, range_len = map(int, line.split(" "))
            if number in range(dest_start, dest_start+range_len):
                return source_start + (number-dest_start)
        return number
    seeds = data.split("seeds: ")[1].split("\n\n")[0].split(" ")
    seed_to_soil = data.split("seed-to-soil map:\n")[1].split("\n\n")[0].split("\n")
    soil_to_fert = data.split("soil-to-fertilizer map:\n")[1].split("\n\n")[0].split("\n")
    fert_to_water = data.split("fertilizer-to-water map:\n")[1].split("\n\n")[0].split("\n")
    water_to_light = data.split("water-to-light map:\n")[1].split("\n\n")[0].split("\n")
    light_to_temp = data.split("light-to-temperature map:\n")[1].split("\n\n")[0].split("\n")
    temp_to_humid = data.split("temperature-to-humidity map:\n")[1].split("\n\n")[0].split("\n")
    humid_to_location = data.split("humidity-to-location map:\n")[1].split("\n\n")[0].split("\n")

    seed_ranges = [(int(seeds[i]), int(seeds[i+1])) for i in range(0, len(seeds), 2)]
    i = 0
    for i in range(0, 10000000000000000):
        location = i
        for func in [humid_to_location, temp_to_humid, light_to_temp, water_to_light, fert_to_water, soil_to_fert, seed_to_soil]:
            location = y_to_x(func, location)
        for seed_start, seed_len in seed_ranges:
            if location in range(seed_start, seed_start+seed_len):
                return i

if __name__ == "__main__":
    with open('Day5\data.txt', 'r') as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2reverse(data)}")