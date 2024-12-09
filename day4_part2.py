if __name__ == "__main__":
    
    file = open("input_day4.txt", 'r')
    ws = []
    square_list = []
    square_count = 0
    allowed = ['MMASS', 'MSAMS', 'SSAMM', 'SMASM']

    for line in file:
        ws.append(line.strip())
    
    for j in range(1, len(ws) - 1): # Loop through lines
        for i in range(1, len(ws[0]) - 1): # Loop through columns
            letter = ws[j][i]
            if  letter == 'A':
                square = ws[j-1][i-1] + ws[j-1][i+1] + ws[j][i] + ws[j+1][i-1] + ws[j+1][i+1]
                square_list.append(square)             
    
    for square in square_list:
        if square in allowed:
            square_count += 1

    print(square_count) 
    print('test')