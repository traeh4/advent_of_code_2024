if __name__ == '__main__':
    with open('day_9/disk_map.txt', 'r') as f:
        disk_map = list(f.readlines()[0])
    final_list = []
    intermediate_list = []
    ultimate_list = []
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
    print(final_list[len(final_list) - 50:])
    for i in range(len(final_list) - 1, -1, -1):
        if final_list[i] in intermediate_list or intermediate_list == []:
            intermediate_list.append(final_list[i])
        else:
            ultimate_list.insert(0, intermediate_list)
            intermediate_list = [final_list[i]]
    ultimate_list.insert(0, intermediate_list)
    for i in range(len(ultimate_list) - 1, -1, -1):
        target_length = len(ultimate_list[i])
        for j in range(i):
            if len(ultimate_list[j]) == target_length and '.' in ultimate_list[j]:
                ultimate_list.pop(j)
                target_list = ultimate_list.pop()
                ultimate_list.insert(j, target_list)



    '''
    for i in range(len(final_list)):
        checksum += i * final_list[i]
    print(checksum)
    '''