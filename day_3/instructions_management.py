import re

def create_python_tuples_from_input():
    muls = []
    
    with open('day_3/corrupted_instructions.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            while re.search(r'mul\([0-9]+,[0-9]+\)', line) != None:
                mul = re.search(r'mul\([0-9]+,[0-9]+\)', line)
                start, end = mul.span()
                mul = line[start:end]
                muls.append(((int(mul[4:mul.index(',')])), int(mul[mul.index(',') + 1:mul.index(')')])))
                line = line.replace(mul, '')
        return muls

'''
Prior iteration - worked but not as fancy

def create_only_do_python_tuples_from_input():
    muls = []
    
    with open('day_3/corrupted_instructions.txt', 'r') as f:
        do_on = True
        for line in f.readlines():
            line = line.rstrip()
            do_on_substring = "do()"
            do_off_substring = "don't()"
            mul_substring = r"^mul\([0-9]+,[0-9]+\)"
            for i in range(len(line)):
                do_candidate = line[i:i + len(do_on_substring)]
                if do_candidate == do_on_substring:
                    do_on = True
                dont_candidate = line[i:i + len(do_off_substring)]
                if dont_candidate == do_off_substring:
                    do_on = False
                if line[i:].count(")") != 0:
                    next_parenthesis = line.index(')', i)
                    mul_substring_candidate = line[i:next_parenthesis + 1]
                if re.search(mul_substring, mul_substring_candidate) and do_on:
                    num_1_start = 4
                    num_1_end = mul_substring_candidate.index(',')
                    num_2_start = mul_substring_candidate.index(',') + 1
                    num_2_end = mul_substring_candidate.index(')')
                    muls.append(((int(mul_substring_candidate[num_1_start:num_1_end])), int(mul_substring_candidate[num_2_start:num_2_end])))
    return muls
'''

def create_only_do_python_tuples_from_input():
    muls = []

    with open('day_3/corrupted_instructions.txt', 'r') as f:
        do_on = True
        for line in f.readlines():
            line = line.rstrip()
            target_substrings = r"(do\(\)|don't\(\)|mul\([0-9]+,[0-9]+\))"
            matches = re.findall(target_substrings, line)
            for match in matches:
                if match == "do()":
                    do_on = True
                elif match == "don't()":
                    do_on = False
                elif do_on:
                    muls.append((int(match[4:match.index(',')]), int(match[match.index(',') + 1:match.index(')')])))
    
    return muls

if __name__ == '__main__':
    #muls = create_python_tuples_from_input()
    #print(muls)
    muls = create_only_do_python_tuples_from_input()
    print(muls)