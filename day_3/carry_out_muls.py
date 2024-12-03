import instructions_management

if __name__ == '__main__':
    total = 0
    muls = instructions_management.create_python_tuples_from_input()
    for mul in muls:
        total += mul[0] * mul[1]
    print(total)
