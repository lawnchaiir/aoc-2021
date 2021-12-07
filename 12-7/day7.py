
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

distances = {}

for i in range(upper_bound):
    sum = 0

    for pos in crab_sub_positions:
        distance = abs(i - pos)
        if distance in distances:
            sum += distances[distance]
            continue

        if pos > i:
            direction = -1
        elif pos < i:
            direction = 1

        fuel_cost = 1
        curr_cost = 0
        while pos != i:
            curr_cost += fuel_cost
            pos += direction
            fuel_cost += 1

        sum += curr_cost
        distances[distance] = curr_cost

    if sum < total_fuel:
        total_fuel = sum
        best_pos = i

print(total_fuel, best_pos)