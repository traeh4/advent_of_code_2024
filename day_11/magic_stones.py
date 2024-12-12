def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
            continue
        if len(list(str(stone))) % 2 == 0:
            sub_stone_lengths = len(list(str(stone))) // 2
            new_stone_1 = int(str(stone)[:sub_stone_lengths])
            new_stone_2 = int(str(stone)[sub_stone_lengths:])
            new_stones.append(new_stone_1)
            new_stones.append(new_stone_2)
            continue
        stone *= 2024
        new_stones.append(stone)
    return new_stones

if __name__ == '__main__':
    stones = [int(i) for i in '4 4841539 66 5279 49207 134 609568 0'.split(' ')]
    for i in range(25):
        stones = blink(stones)
    print(len(stones))
