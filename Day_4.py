if __name__ == '__main__':
    # Import txt file
    file = open('input_day_4.txt', 'r')
    word_search = []
    for line in file:
        word_search.append(line.strip())
    all_words = []
    len_col = len(word_search)
    len_row = len(word_search[0])
    right = False
    left = False
    up = False
    down = False
    for j in range(len(word_search[0])): # Run through line
        for i in range(len(word_search)): # Run through columns
            # Check right
            if i < len_row - 3:
                word = word_search[j][i:i+4]
                all_words.append(word)
                right = True
            # Check left
            if i > 2:
                word = word_search[j][i] + word_search[j][i-1] + word_search[j][i-2] + word_search[j][i-3]
                all_words.append(word)
                left = True
            # Check up
            if j > 2:
                word = word_search[j][i] + word_search[j-1][i] + word_search[j-2][i] + word_search[j-3][i]
                all_words.append(word)
                up = True
            # Check down
            if j < len_col - 3:
                word = word_search[j][i] + word_search[j+1][i] + word_search[j+2][i] + word_search[j+3][i]
                all_words.append(word)
                down = True
            
            # Right up diagonal
            if up and right:
                word = word_search[j][i] + word_search[j-1][i+1] + word_search[j-2][i+2] + word_search[j-3][i+3]
                all_words.append(word)

            # Right down diagonal
            if right and down:
                word = word_search[j][i] + word_search[j+1][i+1] + word_search[j+2][i+2] + word_search[j+3][i+3]
                all_words.append(word)

            # Left up diagonal
            if left and up:
                word = word_search[j][i] + word_search[j-1][i-1] + word_search[j-2][i-2] + word_search[j-3][i-3]
                all_words.append(word)
            
            # Left down diagonal
            if left and down:
                word = word_search[j][i] + word_search[j+1][i-1] + word_search[j+2][i-2] + word_search[j+3][i-3]
                all_words.append(word)

            right = False
            left = False
            top = False
            down = False
    
    xmas_counter = 0 
    for word in all_words:
        if word == 'XMAS':
            xmas_counter += 1
    
    print(xmas_counter)