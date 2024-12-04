if __name__ == '__main__':

    count = 0
    xmas = 'XMAS'
    samx = 'SAMX'
    total_lines = 140

    with open('day_4/word_search.txt', 'r') as f:

        lines = f.readlines()

        for i in range(len(lines)):
            line = lines[i].rstrip()
            for j in range(len(line) - 3):
                
                # Find all horizontal XMASes
                if line[j:j + 4] == xmas or line[j:j + 4] == samx:
                    count += 1
                
                # Find all down-and-forward-diagonal XMASes
                if i <= total_lines - 4:
                    line_2 = lines[i + 1].rstrip()
                    line_3 = lines[i + 2].rstrip()
                    line_4 = lines[i + 3].rstrip()
                    down_and_forward_diagonal = line[j] + line_2[j + 1] + line_3[j + 2] + line_4[j + 3]
                    if down_and_forward_diagonal == xmas or down_and_forward_diagonal == samx:
                        count += 1
                
                # Find all up-and-forward-diagonal XMASes
                if i >= 3:
                    line_2 = lines[i - 1].rstrip()
                    line_3 = lines[i - 2].rstrip()
                    line_4 = lines[i - 3].rstrip()
                    up_and_forward_diagonal = line[j] + line_2[j + 1] + line_3[j + 2] + line_4[j + 3]
                    if up_and_forward_diagonal == xmas or up_and_forward_diagonal == samx:
                        count += 1
            
            for j in range(len(line)):
                
                # Find all straight-up-and-down XMASes
                if i <= total_lines - 4:
                    line_2 = lines[i + 1].rstrip()
                    line_3 = lines[i + 2].rstrip()
                    line_4 = lines[i + 3].rstrip()
                    straight_down = line[j] + line_2[j] + line_3[j] + line_4[j]
                    if straight_down == xmas or straight_down == samx:
                            count += 1

        print(count)