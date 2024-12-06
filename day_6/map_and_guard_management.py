def get_python_lists_from_input():
    map_rows = []
    with open('day_6/map.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            map_rows.append(line)
    return map_rows

class guard:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.locs_visited = [self.position]
    def query_forward(self):
        match self.direction:
            case 'north':
                if self.position[0] >= 0:
                    return self.position[0] - 1, self.position[1]
            case 'east':
                if self.position[1] < 129:
                    return self.position[0], self.position[1] + 1
            case 'south':
                if self.position[0] < 129:
                    return self.position[0] + 1, self.position[1]
            case 'west':
                if self.position[1] >= 0:
                    return self.position[0], self.position[1] - 1
        return 'exit', 'exit'
    def turn(self):
        match self.direction:
            case 'north':
                self.direction = 'east'
            case 'east':
                self.direction = 'south'
            case 'south':
                self.direction = 'west'
            case 'west':
                self.direction = 'north'
    def advance(self):
        match self.direction:
            case 'north':
                self.position = [self.position[0] - 1, self.position[1]]
            case 'east':
                self.position = [self.position[0], self.position[1] + 1]
            case 'south':
                self.position = [self.position[0] + 1, self.position[1]]
            case 'west':
                self.position = [self.position[0], self.position[1] - 1]
        if self.position not in self.locs_visited:
            self.locs_visited.append(self.position)
    def get_locs_visited(self):
        return self.locs_visited
    def __str__(self):
        print("Hup, hup, hup, hup...")

def junk_map():
    return [
        '....#.....',
        '.........#',
        '..........',
        '..#.......',
        '.......#..',
        '..........',
        '.#..^.....',
        '........#.',
        '#.........',
        '......#...',
    ]