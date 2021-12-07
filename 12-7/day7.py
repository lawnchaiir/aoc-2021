
crab_sub_positions = []

upper_bound = -1

with open("input.txt", "r") as f:
    line = f.read().split(",")
    
    for v in line:
        pos = int(v)
        upper_bound = max(upper_bound, pos)
        crab_sub_positions.append(pos)


best_pos = upper_bound
total_fuel = 0xFFFFFFFF

for i in range(upper_bound):
    sum = 0
    for pos in crab_sub_positions:
        delta = abs(pos - i)
        sum += delta
    
    if sum < total_fuel:
        total_fuel = sum
        best_pos = i

print(total_fuel, best_pos)