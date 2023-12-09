def part1(data):
    def calc_layers(layers, history):
        layer = []
        for i in range(1, len(history), 1):
            layer.append(history[i-1] - history[i])
        layers.append(layer)
        if list(set(layer)) == [0]:
            return layers
        else:
            return calc_layers(layers, layer)
    ans = 0 
    for history in data:
        history = list(map(int, history.split(" ")))
        history.reverse()
        layers = [history]
        layers = calc_layers(layers, history)
        layers.reverse()
        for i, layer in enumerate(layers):
            if i == 0:
                layer.append(0)
            else:
                layer.insert(0, layers[i-1][0] + layer[0])
        ans += layers[-1][0]
    return ans
        

def part2(data):
    def calc_layers(layers, history):
        layer = []
        for i in range(1, len(history), 1):
            layer.append(history[i-1] - history[i])
        layers.append(layer)
        if list(set(layer)) == [0]:
            return layers
        else:
            return calc_layers(layers, layer)
    ans = 0 
    for history in data:
        history = list(map(int, history.split(" ")))
        layers = [history]
        layers = calc_layers(layers, history)
        layers.reverse()
        for i, layer in enumerate(layers):
            if i == 0:
                layer.append(0)
            else:
                layer.insert(0, layers[i-1][0] + layer[0])
        ans += layers[-1][0]
    return ans

if __name__ == "__main__":
    with open('Day9\exampledata.txt', 'r') as f:
        data = f.read()
    data = data.split("\n")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")