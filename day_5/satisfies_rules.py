def format_rules_from_input():
    rules = []
    with open('day_5/ordering_rules.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip().split('|')
            line = [int(i) for i in line]
            rules.append(line)
    return rules

def format_pages_from_input():
    pages = []
    with open('day_5/pages_to_produce.txt', 'r') as f:
        for line in f.readlines():
            line = line.rstrip().split(',')
            line = [int(i) for i in line]
            pages.append(line)
    return pages

def satisfies(rule, order):
    if rule[0] not in order or rule[1] not in order:
        return True
    if order.index(rule[0]) < order.index(rule[1]):
        return True
    return False

def page_satisfies(rules, page):
    satisfy = True
    for rule in rules:
        if not satisfies(rule, page):
            satisfy = False
    return satisfy

if __name__ == '__main__':
    pages = format_pages_from_input()
    rules = format_rules_from_input()
    print(satisfies([93, 95], pages[-1]))
    print(page_satisfies(rules, pages[1]))