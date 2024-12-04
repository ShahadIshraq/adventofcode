
def is_line_safe(line):
    increasing = all(line[i] < line[i + 1] for i in range(len(line) - 1))
    decreasing = all(line[i] > line[i + 1] for i in range(len(line) - 1))
    if not increasing and not decreasing:
        return False
    
    # difference two adjacent items can not be more than 3
    for i in range(len(line) - 1):
        if abs(line[i] - line[i + 1]) > 3:
            return False
    return True
    


with open('input', 'r') as file:
    lines = file.readlines()

safe_lines = 0
for line in lines:
    current_line = list(map(int, line.split()))
    # check if items in the current list are increasing or decreasing
    if is_line_safe(current_line):
        safe_lines += 1
        continue

    # call is_line_safe by removing only one item at a time from the start
    for i in range(len(current_line)):
        if is_line_safe(current_line[:i] + current_line[i + 1:]):
            safe_lines += 1
            break

print(safe_lines)
