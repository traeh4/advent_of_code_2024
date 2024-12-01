import lists_management

if __name__ == '__main__':
    total = 0
    left_list, right_list = lists_management.create_python_lists_from_input()
    left_list.sort()
    right_list.sort()
    for i, (left, right) in enumerate(zip(left_list, right_list)):
        distance_at_this_level = abs(left - right)
        total += distance_at_this_level
    print(total)
