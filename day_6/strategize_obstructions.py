import map_and_guard_management

def twenty_thousand_steps(map_rows):
    guard = map_and_guard_management.guard([54, 56], 'north')
    forward_row, forward_column = guard.query_forward()
    forward_item = map_rows[forward_row][forward_column]
    step_count = 0
    while forward_row != 'exit' and step_count <= 20000:
        forward_item = map_rows[forward_row][forward_column]
        if forward_item == '.':
            guard.advance()
            step_count += 1
        if forward_item == '#':
            guard.turn()
        forward_row, forward_column = guard.query_forward()
        if forward_row == 'exit':
            return False
    return True

# This takes a while
if __name__ == '__main__':
    map_rows = map_and_guard_management.get_python_lists_from_input()
    obstruction_targets = []
    for row_loc in range(len(map_rows)):
        for column_loc in range(len(map_rows[row_loc])):
            trial_map = map_and_guard_management.get_python_lists_from_input()
            row = trial_map.pop(54)
            row = row[:56] + "." + row[57:]
            trial_map.insert(54, row)
            if trial_map[row_loc][column_loc] == '.':
                row = trial_map.pop(row_loc)
                row = row[:column_loc] + "#" + row[column_loc + 1:]
                trial_map.insert(row_loc, row)
                if twenty_thousand_steps(trial_map):
                    obstruction_targets.append([row_loc, column_loc])
    # Subtract 1 because I did not exclude the guard's starting point
    print(len(obstruction_targets) - 1)