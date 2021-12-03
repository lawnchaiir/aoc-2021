

with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i])

count = 0
for i in range(1, len(lines)):
    if lines[i] > lines[i-1]:
        count += 1

print(count)

prev_sum = 0
count = 0
for i in range(3, len(lines)):
    sl = lines[i - 3: i]
    curr_sum = sum(sl)
    if curr_sum > prev_sum:
        count += 1
    prev_sum = curr_sum

print(count)

