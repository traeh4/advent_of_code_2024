import instructions_management
import operator
import random

if __name__ == '__main__':
    instructions = instructions_management.get_python_dict_from_input()
    operators = [operator.add, operator.mul]
    total = 0
    for test_val, nums in instructions.items():
        test_val = int(test_val)
        tests = []
        valid = False
        num_tests = 2**(len(nums) - 1)
        while len(tests) < num_tests:
            test = random.choices(operators, k = len(nums) - 1)
            if test not in tests:
                tests.append(test)
        for test in tests:
            for i in range(len(nums) - 1):
                op = test[i]
                if i == 0:
                    local_total = op(nums[i], nums[i + 1])
                else:
                    local_total = op(local_total, nums[i + 1])
            if local_total == test_val:
                valid = True
        if valid:
            total += test_val
    print(total)