if __name__ == '__main__':
    import re
    
    # Import txt file
    file = open('input_day_3.txt', 'r')
    input_string = file.read().replace("\n", "")
    mul_matches = []
    sol = 0
    for match in re.findall(r"mul\((\d+,\d+)\)", input_string):
        mul_matches.append(match)
    for match in mul_matches:
        numbers = match.split(',')
        sol += int(numbers[0]) * int(numbers[1])
    
    print(sol)
    
    mul_data = []
    mul_idx_number = {}
    do_matches = []
    do_start_idx = []
    dont_matches = []
    dont_start_idx = []
    sol2 = 0
    for match in re.finditer(r"mul\((\d+,\d+)\)", input_string):
        mul_data.append(match)
        mul_idx_number[match.start()] = match.group(1)
    for match in re.finditer(r"do\(\)", input_string):
        do_matches.append(match)
        do_start_idx.append(match.start())

    for match in re.finditer(r"don\'t\(\)", input_string):
        dont_matches.append(match)
        dont_start_idx.append(match.start())

    do = True
    for i in range(len(input_string)):
        if do:
            if i in dont_start_idx:
                do = False
        else:
            if i in do_start_idx:
                do = True
        if do:
            if i in list(mul_idx_number.keys()):
                numbers = mul_idx_number[i].split(',')
                sol2 += int(numbers[0]) * int(numbers[1])
    print(sol2)