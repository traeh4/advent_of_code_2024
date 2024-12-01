import lists_management

if __name__ == '__main__':
    total = 0
    left_list, right_list = lists_management.create_python_lists_from_input()
    for item in left_list:
        right_count = right_list.count(item)
        similarity_score = item * right_count
        total += similarity_score
    print(total)