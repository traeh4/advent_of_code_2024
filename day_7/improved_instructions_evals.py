import instructions_management
import operator

def build_tests(operators, length, current_test, all_tests):
    if len(current_test) == length:
        all_tests.append(current_test)
        return all_tests
    for operator in operators:
        build_tests(operators, length, current_test + [operator], all_tests)
    return all_tests

def concatenate(a, b):
    return int(str(a) + str(b))

if __name__ == '__main__':
    instructions = instructions_management.get_python_dict_from_input()
    operators = [operator.add, operator.mul, concatenate]
    total = 0
    for test_val, nums in instructions.items():
        test_val = int(test_val)
        valid = False
        tests = build_tests(operators, len(nums) - 1, [], [])
        for test in tests:
            for i in range(len(nums) - 1):
                op = test[i]
                if i == 0:
                    local_total = op(nums[i], nums[i + 1])
                else:
                    local_total = op(local_total, nums[i + 1])
            if local_total == test_val:
                valid = True
                break
        if valid:
            total += test_val
    print(total)