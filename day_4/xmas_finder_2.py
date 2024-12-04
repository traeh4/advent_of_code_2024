if __name__ == '__main__':

    count = 0
    mas = 'MAS'
    sam = 'SAM'

    with open('day_4/word_search.txt', 'r') as f:

        lines = f.readlines()

        for i in range(len(lines) - 2):
            
            line = lines[i].rstrip()
            line_2 = lines[i + 1].rstrip()
            line_3 = lines[i + 2].rstrip()
            
            for j in range(len(line) - 2):
                down_and_right = line[j] + line_2[j + 1] + line_3[j + 2]
                down_and_left = line[j + 2] + line_2[j + 1] + line_3[j]
                if (down_and_right == mas or down_and_right == sam) and\
                    (down_and_left == mas or down_and_left == sam):
                        count += 1

        print(count)