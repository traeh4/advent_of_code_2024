def create_python_lists_from_input():
    line_1 = []
    line_2 = []
    
    with open('day_1/lists.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip().split('   ')
            line = [int(i) for i in line]
            line_1.append(line[0])
            line_2.append(line[1])
    
    return line_1, line_2

if __name__ == '__main__':
    line_1, line_2 = create_python_lists_from_input()
    print(line_1)
    print(line_2)