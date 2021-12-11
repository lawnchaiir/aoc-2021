

with open("input.txt", "r") as f:
    lines = []
    for line in f:
        row = [int(c) for c in line if not c.isspace()]
        lines.append(row)

row_length = len(row)

def isLowestOfNeighbors(x, y):
    val = lines[x][y]
    for xOffset in range(-1, 2):
        currX = x + xOffset
        if currX < 0 or currX >= len(lines):
            continue
        for yOffset in range(-1, 2):
            currY = y + yOffset
            if currY < 0 or currY >= row_length:
                continue
            if x == currX and y == currY:
                continue
            compare_val = lines[currX][currY]
            if compare_val < val:
                return False
    return True

lowest_coords = []
for x, row in enumerate(lines):
   for y, val in enumerate(row):
       if isLowestOfNeighbors(x, y):
           lowest_coords.append((x, y))


total_risk = 0
for coord in lowest_coords:
    x, y = coord
    val = lines[x][y]

    risk_level = val + 1
    total_risk += risk_level

print(total_risk)
