import reports_management

def increasing_or_decreasing(report):
    increasing = False
    decreasing = False

    for i in range(1, len(report)):
        if report[i] > report[i - 1]:
            increasing = True
        else:
            increasing = False
            break
    
    for i in range(1, len(report)):
        if report[i] < report[i - 1]:
            decreasing = True
        else:
            decreasing = False
            break
    
    if increasing:
        return 'increasing'
    if decreasing:
        return 'decreasing'
    else:
        return False

def increasing_safely(report):
    safe = False
    
    for i in range(1, len(report)):
        if report[i] - report[i - 1] in [1, 2, 3]:
            safe = True
        else:
            safe = False
            break
    
    return safe

def decreasing_safely(report):
    safe = False
    
    for i in range(1, len(report)):
        if report[i - 1] - report[i] in [1, 2, 3]:
            safe = True
        else:
            safe = False
            break
    
    return safe

if __name__ == '__main__':
    reports = reports_management.create_python_lists_from_input()
    count = 0
    for report in reports:
        if increasing_or_decreasing(report) == 'increasing':
            if increasing_safely(report):
                count += 1
        if increasing_or_decreasing(report) == 'decreasing':
            if decreasing_safely(report):
                count += 1
    print(count)