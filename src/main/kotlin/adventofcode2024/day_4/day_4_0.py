# direction enum
class Direction:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    UP_LEFT = 4
    UP_RIGHT = 5
    DOWN_LEFT = 6
    DOWN_RIGHT = 7

    def get_name(direction):
        if direction == Direction.UP:
            return "UP"
        elif direction == Direction.DOWN:
            return "DOWN"
        elif direction == Direction.LEFT:
            return "LEFT"
        elif direction == Direction.RIGHT:
            return "RIGHT"
        elif direction == Direction.UP_LEFT:
            return "UP_LEFT"
        elif direction == Direction.UP_RIGHT:
            return "UP_RIGHT"
        elif direction == Direction.DOWN_LEFT:
            return "DOWN_LEFT"
        elif direction == Direction.DOWN_RIGHT:
            return "DOWN_RIGHT"


def check(input, i, j, direction):
    # given the position (i, j) in the 2D array, check "XMAS" is found at that position in given direction
    # return True if found, False otherwise
    if input[i][j] != 'X':
        return False
    
    if direction == Direction.UP:
        if i-3 >= 0:
            return input[i-1][j] == 'M' and input[i-2][j] == 'A' and input[i-3][j] == 'S'
    elif direction == Direction.DOWN:
        if i+3 < len(input):
            return input[i+1][j] == 'M' and input[i+2][j] == 'A' and input[i+3][j] == 'S'
    elif direction == Direction.LEFT:
        if j-3 >= 0:
            return input[i][j-1] == 'M' and input[i][j-2] == 'A' and input[i][j-3] == 'S'
    elif direction == Direction.RIGHT:
        if j+3 < len(input[i]):
            return input[i][j+1] == 'M' and input[i][j+2] == 'A' and input[i][j+3] == 'S'
    elif direction == Direction.UP_LEFT:
        if i-3 >= 0 and j-3 >= 0:
            return input[i-1][j-1] == 'M' and input[i-2][j-2] == 'A' and input[i-3][j-3] == 'S'
    elif direction == Direction.UP_RIGHT:
        if i-3 >= 0 and j+3 < len(input[i]):
            return input[i-1][j+1] == 'M' and input[i-2][j+2] == 'A' and input[i-3][j+3] == 'S'
    elif direction == Direction.DOWN_LEFT:
        if i+3 < len(input) and j-3 >= 0:
            return input[i+1][j-1] == 'M' and input[i+2][j-2] == 'A' and input[i+3][j-3] == 'S'
    elif direction == Direction.DOWN_RIGHT:
        if i+3 < len(input) and j+3 < len(input[i]):
            return input[i+1][j+1] == 'M' and input[i+2][j+2] == 'A' and input[i+3][j+3] == 'S'
    return False
    


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
        for direction in range(8):
            if check(input, i, j, direction):
                print(f"({i}, {j}) : {Direction.get_name(direction)}")
                count += 1

print(count)
