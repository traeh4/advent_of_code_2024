if __name__ == '__main__':
    with open('day_9/disk_map.txt', 'r') as f:
        disk_map = list(f.readlines()[0])
    first_round = []
    second_round = []
    third_round = []
    checksum = 0
    free_spaces = [disk_map[i] for i in range(1, len(disk_map), 2)]
    file_lengths = [disk_map[i] for i in range(0, len(disk_map), 2)]
    for i in range(len(free_spaces)):
        for j in range(int(file_lengths[i])):
            first_round.append(i)
        for j in range(int(free_spaces[i])):
            first_round.append('.')
    for j in range(int(file_lengths[len(free_spaces)])):
        first_round.append(len(free_spaces))
    for i in range(len(first_round) - 1, -1, -1):
        if first_round[i] in second_round or second_round == []:
            second_round.append(first_round[i])
        else:
            third_round.insert(0, second_round)
            second_round = [first_round[i]]
    third_round.insert(0, second_round)
    iterator = len(third_round) - 1
    file_block = []
    while 0 not in file_block:
        file_block = third_round.pop(iterator)
        target_length = len(file_block)
        found_empty_space = False
        if '.' in file_block:
            third_round.insert(iterator, file_block)
            iterator -= 1
            continue
        for j in range(iterator):
            if len(third_round[j]) >= target_length and '.' in third_round[j]:
                found_empty_space = True
                empty_space = third_round.pop(j)
                empty_space_size = len(empty_space)
                if empty_space_size == target_length:
                    third_round.insert(j, file_block)
                else:
                    for k in range(target_length):
                        empty_space.remove('.')
                    third_round.insert(j, empty_space)
                    third_round.insert(j, file_block)
                    iterator += 1
                third_round.insert(iterator, ['.' for i in range(target_length)])
                if '.' in third_round[iterator - 1]:
                    grab = third_round.pop(iterator)
                    third_round[iterator - 1] += grab
                    iterator -= 1
                    if iterator + 1 in range(len(third_round)) and '.' in third_round[iterator + 1]:
                        grab = third_round.pop(iterator)
                        third_round[iterator] += grab
                if iterator + 1 in range(len(third_round)) and '.' in third_round[iterator + 1]:
                    grab = third_round.pop(iterator)
                    third_round[iterator] += grab
                break
        if not found_empty_space:
            third_round.insert(iterator, file_block)
        iterator -= 1
    ultimate_round = []
    for item in third_round:
        for subitem in item:
            ultimate_round.append(subitem)
    for i in range(len(ultimate_round)):
        if ultimate_round[i] != '.':
            checksum += i * ultimate_round[i]
    print(checksum)
