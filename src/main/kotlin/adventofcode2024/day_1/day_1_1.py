
# read input file and load into two lists
with open('input', 'r') as file:
    lines = file.readlines()


list1 = []
list2_dict = {}

for line in lines:
    line_parts = line.split()
    list1.append(int(line_parts[0]))
    list_2_item = int(line_parts[1])

    list2_dict[list_2_item] = list2_dict.get(list_2_item, 0) + 1


# iterate over each index of the queues and find the sum of differences as each index
sum = 0
for i in list1:
    sum += i * list2_dict.get(i, 0)

print(sum)
