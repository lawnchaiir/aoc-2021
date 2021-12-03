

with open("input.txt", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i])

count = 0
for i in range(1, len(lines)):
    if lines[i] > lines[i-1]:
        count += 1

print(count)