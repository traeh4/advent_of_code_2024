def get_python_list_from_input():
    with open('day_10/map.txt', 'r') as f:
        return [list(line.rstrip()) for line in f.readlines()]

class trail_finder:
    def __init__(self, trailhead_loc):
        self.trailhead_loc = trailhead_loc
        self.loc = trailhead_loc
        self.map = get_python_list_from_input()
        self.hiking_trails = []
    def get_adjacent_locs(self):
        self.adjacent_locs = [[self.loc[0] + 1, self.loc[1]], [self.loc[0] - 1, self.loc[1]], [self.loc[0], self.loc[1] + 1], [self.loc[0], self.loc[1] - 1]]
        if self.loc[0] == 0:
            self.adjacent_locs.remove([self.loc[0] - 1, self.loc[1]])
        if self.loc[0] == 46:
            self.adjacent_locs.remove([self.loc[0] + 1, self.loc[1]])
        if self.loc[1] == 0:
            self.adjacent_locs.remove([self.loc[0], self.loc[1] - 1])
        if self.loc[1] == 46:
            self.adjacent_locs.remove([self.loc[0], self.loc[1] + 1])
        return self.adjacent_locs
    def get_hiking_appropriate_adjacent_locs(self):
        self.hiking_appropriate_adjacent_locs = []
        values = [int(self.get_elevation(adjacent_loc)) for adjacent_loc in self.get_adjacent_locs()]
        for mapped_loc in zip(values, self.get_adjacent_locs()):
            if mapped_loc[0] == int(self.get_elevation(self.loc)) + 1:
                self.hiking_appropriate_adjacent_locs.append(mapped_loc[1])
        return self.hiking_appropriate_adjacent_locs
    def move_to_next_loc(self, next_loc):
        self.hiking_appropriate_adjacent_locs = []
        self.loc = next_loc
    def get_elevation(self, query_loc):
        return self.map[query_loc[0]][query_loc[1]]
    def get_hiking_trails(self):
        return self.hiking_trails
    def find_hiking_trails(self):
        if self.get_elevation(self.loc) == '9':
            if self.loc not in self.hiking_trails:
                self.hiking_trails.append(self.loc)       
        if self.get_hiking_appropriate_adjacent_locs() == []:
            return None
        for query_loc in self.get_hiking_appropriate_adjacent_locs():
            self.move_to_next_loc(query_loc)
            self.find_hiking_trails()
    def find_hiking_trail(self, hiking_trail):
        if self.get_elevation(self.loc) == '9':
            self.hiking_trails.append(hiking_trail)
        if self.get_hiking_appropriate_adjacent_locs() == []:
            return None
        for query_loc in self.get_hiking_appropriate_adjacent_locs():
            self.move_to_next_loc(query_loc)
            self.find_hiking_trail(hiking_trail)

if __name__ == '__main__':
    map = get_python_list_from_input()
    print(map)
    print(len(map), len(map[0]))
    trailhead = trail_finder([2, 0])
    trailhead.find_hiking_trails()
    print(trailhead.get_hiking_trails())

    