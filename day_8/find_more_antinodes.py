import map_management

if __name__ == '__main__':
    map = map_management.get_python_lists_from_input()
    frequency_dict = {}
    antinodes = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] != '.':
                if map[i][j] not in frequency_dict:
                    frequency_dict[map[i][j]] = []
                frequency_dict[map[i][j]].append([i, j])
    for antenna, locs in frequency_dict.items():
        for loc in locs:
            if loc not in antinodes:
                antinodes.append(loc)
        for i in range(len(locs) - 1):
            for j in range(i + 1, len(locs)):
                vector = map_management.distance(locs[i], locs[j])
                antinode_1 = [locs[j][0] + vector[0], locs[j][1] + vector[1]]
                while antinode_1[0] in range(50) and antinode_1[1] in range(50):
                    if antinode_1 not in antinodes:
                        antinodes.append(antinode_1)
                    new_loc = antinode_1
                    antinode_1 = [new_loc[0] + vector[0], new_loc[1] + vector[1]]
                vector = map_management.distance(locs[j], locs[i])
                antinode_2 = [locs[i][0] + vector[0], locs[i][1] + vector[1]]
                while antinode_2[0] in range(50) and antinode_2[1] in range(50):
                    if antinode_2 not in antinodes:
                        antinodes.append(antinode_2)
                    new_loc = antinode_2
                    antinode_2 = [new_loc[0] + vector[0], new_loc[1] + vector[1]]
    print(len(antinodes))
    