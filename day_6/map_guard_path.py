import map_and_guard_management

# This gives an answer 1 more than the correct solution. I am not sure why.
if __name__ == '__main__':
    map_rows = map_and_guard_management.get_python_lists_from_input()
    guard = map_and_guard_management.guard([54, 56], 'north')
    row = map_rows.pop(54)
    row = row[:56] + "." + row[57:]
    map_rows.insert(54, row)
    forward_row, forward_column = guard.query_forward()
    forward_item = map_rows[forward_row][forward_column]
    while forward_row != 'exit':
        forward_item = map_rows[forward_row][forward_column]
        if forward_item == '.':
            guard.advance()
        if forward_item == '#':
            guard.turn()
        forward_row, forward_column = guard.query_forward()
    print(len(guard.get_locs_visited()))