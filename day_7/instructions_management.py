def get_python_dict_from_input():
    
    instruction_dict = {}
    with open('day_7/calibration_instructions.txt', 'r') as f:
        lines = f.readlines()
        for row in range(len(lines)):
            line = lines[row].rstrip()
            test_value = int(line.split(': ')[0])
            numbers = [int(i) for i in line.split(': ')[1].split(' ')]
            if test_value in instruction_dict:
                instruction_dict[str(test_value)] = numbers
            else:
                instruction_dict[test_value] = numbers
    return instruction_dict

def dummy_dict():
    return {
        190: [10, 19],
        3267: [81, 40, 27],
        83: [17, 5],
        156: [15, 6],
        7290: [6, 8, 6, 15],
        161011: [16, 10, 13],
        192: [17, 8, 14],
        21037: [9, 7, 18, 13],
        292: [11, 6, 16, 20]
    }

def dummy_dict_2():
    return {
        2062685184: [86, 506, 896, 49, 71],
        5497711: [916, 27, 5, 6, 61],
        4843144705533: [5, 4, 2, 978, 173, 85, 5, 30, 4],
        1583583985017: [9, 1, 744, 7, 6, 132, 83, 4, 5, 6],
        40723: [3, 300, 772, 3],
        469581507: [59, 2, 3, 284, 931],
        108864: [393, 6, 96, 27],
    }

if __name__ == '__main__':
    lst = get_python_dict_from_input()
    #lst = dummy_dict()
    #print(lst)