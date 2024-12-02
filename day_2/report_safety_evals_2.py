import reports_management

def increasing_safely(report):
    safe = False
    
    for i in range(1, len(report)):
        if report[i] - report[i - 1] in [1, 2, 3]:
            safe = True
        else:
            safe = False
            break
    
    return safe

def problem_dampener_inc(report):
    
    for i in range(len(report)):
        trial_report = report.copy()
        trial_report.pop(i)
        if increasing_safely(trial_report):
            return True
    
    return False

def decreasing_safely(report):
    safe = False
    
    for i in range(1, len(report)):
        if report[i - 1] - report[i] in [1, 2, 3]:
            safe = True
        else:
            safe = False
            break
    
    return safe

def problem_dampener_dec(report):
    
    for i in range(len(report)):
        trial_report = report.copy()
        trial_report.pop(i)
        if decreasing_safely(trial_report):
            return True
    
    return False

if __name__ == '__main__':
    reports = reports_management.create_python_lists_from_input()
    count = 0
    for report in reports:
        if problem_dampener_inc(report):
            count += 1
        if problem_dampener_dec(report):
            count += 1
    print(count)