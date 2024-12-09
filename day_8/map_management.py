def get_python_lists_from_input():
    with open('day_8/map.txt', 'r') as f:
        return [list(line.rstrip()) for line in f.readlines()]

def distance(a, b):
    return [b[0] - a[0], b[1] - a[1]]

if __name__ == '__main__':
    map = get_python_lists_from_input()
    print(len(map), len(map[5]))
    