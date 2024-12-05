import satisfies_rules

if __name__ == '__main__':
    
    pages = satisfies_rules.format_pages_from_input()
    #pages = [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [64, 19, 4, 7, 8], [19, 4, 7, 8, 5]]
    rules = satisfies_rules.format_rules_from_input()
    total = 0
    
    for page in pages:
        if satisfies_rules.page_satisfies(rules, page):
            total += page[len(page) // 2]

    print(total)