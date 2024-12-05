import satisfies_rules

def rearrange(rules, page):
    for rule in rules:
        if rule[0] in page and rule[1] in page and page.index(rule[0]) > page.index(rule[1]):
            distal = page.pop(page.index(rule[0]))
            page.insert(page.index(rule[1]), distal)
    return page

def page_satisfies(rules, page):
    satisfies = True
    for rule in rules:
        if not satisfies_rules.satisfies(rule, page):
            satisfies = False
    return satisfies

if __name__ == '__main__':
    
    pages = satisfies_rules.format_pages_from_input()
    rules = satisfies_rules.format_rules_from_input()
    incorrectly_ordered = []
    total = 0
    
    for page in pages:
        satisfies = True
        for rule in rules:
            if not satisfies_rules.satisfies(rule, page):
                satisfies = False
        if not satisfies:
            incorrectly_ordered.append(page)

    for page in incorrectly_ordered:
        rearranged_page = page.copy()
        while not page_satisfies(rules, rearranged_page):
            rearranged_page = rearrange(rules, rearranged_page)
        total += rearranged_page[len(rearranged_page) // 2]
    
    print(total)