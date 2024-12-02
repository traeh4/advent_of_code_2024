def create_python_lists_from_input():
    reports = []
    
    with open('day_2/reports.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip().split(' ')
            line = [int(i) for i in line]
            reports.append(line)
    
    return reports

if __name__ == '__main__':
    reports = create_python_lists_from_input()
    print(reports)