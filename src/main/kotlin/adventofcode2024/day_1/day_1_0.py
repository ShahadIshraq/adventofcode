from queue import PriorityQueue

# read input file and load into two lists
with open('input', 'r') as file:
    lines = file.readlines()


queue1 = PriorityQueue()
queue2 = PriorityQueue()

for line in lines:
    line_parts = line.split()
    queue1.put(int(line_parts[0]))
    queue2.put(int(line_parts[1]))


# iterate over each index of the queues and find the sum of differences as each index
sum_of_differences = 0
for i in range(queue1.qsize()):
    sum_of_differences += abs(queue1.get() - queue2.get())

print(sum_of_differences)
