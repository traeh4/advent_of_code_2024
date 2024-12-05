import satisfies_rules

if __name__ == '__main__':
    
    pages = satisfies_rules.format_pages_from_input()
    #pages = [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [64, 19, 4, 7, 8], [19, 4, 7, 8, 5]]
    rules = satisfies_rules.format_rules_from_input()
    correctly_ordered = []
    total = 0
    
    for page in pages:
        satisfies = True
        for rule in rules:
            if not satisfies_rules.satisfies(rule, page):
                satisfies = False
        if satisfies:
            correctly_ordered.append(page)
    
    for page in correctly_ordered:
        total += page[len(page) // 2]
    print(total)