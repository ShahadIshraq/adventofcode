def check(input, i, j):
    if i < 1 or i > len(input) - 2 or j < 1 or j > len(input[i]) - 2:
        return False
    
    if input[i][j] != 'A':
        return False
    
    return is_valid_diagonal(input[i-1][j-1], input[i+1][j+1]) and is_valid_diagonal(input[i-1][j+1], input[i+1][j-1])


def is_valid_diagonal(char_a, char_b):
    return (char_a == 'M' and char_b == 'S') or (char_a == 'S' and char_b == 'M')
    


# input = """
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# """

# load from input file
input = open('input').read()
input = input.strip().split('\n')

count = 0
for i in range(len(input)):
    for j in range(len(input[i])):
        if check(input, i, j):
            count += 1

print(count)
