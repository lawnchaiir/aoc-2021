
with open("input.txt", "r") as f:
    lines = []
    for line in f:
        row = [int(c) for c in line if not c.isspace()]
        lines.append(row)

row_length = len(row)

def isLowestOfNeighbors(x, y):
    val = lines[x][y]

    offsets = (-1, 0, 1)

    if val == 9:
        return False

    for x_offset in offsets:
        curr_x = x + x_offset
        if curr_x < 0 or curr_x >= len(lines):
            continue
        for y_offset in offsets:
            curr_y = y + y_offset
            # out of bounds
            if curr_y < 0 or curr_y >= row_length:
                continue

            # it's this one
            if x == curr_x and y == curr_y:
                continue

            compare_val = lines[curr_x][curr_y]
            
            # it's a diagonal
            if x_offset * y_offset != 0:
                continue

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

print("total risk", total_risk)


class GraphNode(object):
    nodes = {}

    def __init__(self, x, y):
        self.links = set()
        self.x = x
        self.y = y
        self.value = lines[self.x][self.y]

    def __str__(self):
        return f"{self.x}x{self.y}={self.value}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def connect(self, graph_node):
        if graph_node == self:
            return
        self.links.add((graph_node.x, graph_node.y))
        graph_node.links.add((self.x, self.y))

    def coord(self):
        return (self.x, self.y)

    def add_neighbors(self):
        offsets = (-1, 0, 1)
        for x_offset in offsets:
            curr_x = self.x + x_offset
            if curr_x < 0 or curr_x >= len(lines):
                continue

            for y_offset in offsets:
                curr_y = self.y + y_offset
                if curr_y < 0 or curr_y >= row_length:
                    continue

                if x == curr_x and y == curr_y:
                    continue

                if x_offset * y_offset != 0: # no diagonals
                    continue

                if lines[curr_x][curr_y] == 9:
                    continue

                coord = (curr_x, curr_y)
                if coord not in self.nodes:
                    node = GraphNode(curr_x, curr_y)
                    self.nodes[coord] = node
                else:
                    node = self.nodes[coord]
                self.connect(node)


print("Building graph")
for x, row in enumerate(lines):
   for y, val in enumerate(row):
       coord = (x, y)
       if val == 9:
           continue

       if coord not in GraphNode.nodes:
           node = GraphNode(x, y)
           GraphNode.nodes[coord] = node

for k in GraphNode.nodes:
    node = GraphNode.nodes[k]
    node.add_neighbors()

print("graphed")

basins = []

print("basining")

for coord in lowest_coords:
    basin = []
    nodes_to_visit = []
    
    curr_node = GraphNode.nodes[coord]
    visited = set()

    while curr_node is not None:
        curr_coord = curr_node.coord()
        if curr_coord in visited or curr_node.value == 9:
            if nodes_to_visit:
                next_coord = nodes_to_visit.pop()
                curr_node = GraphNode.nodes[next_coord]
            else:
                curr_node = None
            continue

        visited.add(curr_coord)
        basin.append(curr_coord)
        for link_coord in curr_node.links:
            node = GraphNode.nodes[link_coord]
            if node.value != 9:
                nodes_to_visit.append(link_coord)
                basin.append(link_coord)

        if nodes_to_visit:
            next_coord = nodes_to_visit.pop()
            curr_node = GraphNode.nodes[next_coord]
        else:
            curr_node = None

    basins.append(frozenset(basin))

print("basined")

basins.sort(key=lambda x: len(x), reverse=True)

total = 1

for i in range(3):
    print("Basin length", len(basins[i]))
    total *= len(basins[i])

print(total)