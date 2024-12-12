from functools import cache

def blink(stone):
    if stone == 0:
        return 1
    if len(str(stone)) % 2 == 0:
        sub_stone_lengths = len(str(stone)) // 2
        new_stone_1, new_stone_2 = int(str(stone)[:sub_stone_lengths]), int(str(stone)[sub_stone_lengths:])
        return (new_stone_1, new_stone_2)
    stone *= 2024
    return stone

@cache
def expansion(stone, blinks):
    num_expansion_items = 1
    for i in range(blinks):
        blink_result = blink(stone)
        if isinstance(blink_result, int):
            stone = blink_result
        if isinstance(blink_result, tuple):
            stone = blink_result[0]
            num_expansion_items += expansion(blink_result[1], blinks - i - 1)
    return num_expansion_items


if __name__ == '__main__':
    stones = [int(i) for i in '4 4841539 66 5279 49207 134 609568 0'.split(' ')]
    expansion_lengths = [expansion(i, 75) for i in stones]
    expansion_length = sum(expansion_lengths)
    print(expansion_length)