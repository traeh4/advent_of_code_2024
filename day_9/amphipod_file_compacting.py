if __name__ == '__main__':
    with open('day_9/disk_map.txt', 'r') as f:
        disk_map = list(f.readlines()[0])
    final_list = []
    checksum = 0
    free_spaces = [disk_map[i] for i in range(1, len(disk_map), 2)]
    file_lengths = [disk_map[i] for i in range(0, len(disk_map), 2)]
    for i in range(len(free_spaces)):
        for j in range(int(file_lengths[i])):
            final_list.append(i)
        for j in range(int(free_spaces[i])):
            final_list.append('.')
    for j in range(int(file_lengths[len(free_spaces)])):
        final_list.append(len(free_spaces))
    while '.' in final_list:
        item = final_list.pop()
        if item != '.':
            final_list[final_list.index('.')] = item
    for i in range(len(final_list)):
        checksum += i * final_list[i]
    print(checksum)