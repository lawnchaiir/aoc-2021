import copy

with open("input.txt", "r") as f:
    lines = []
    for line in f:
        row = [int(c) for c in line if not c.isspace()]
        lines.append(row)

steps = 100


class Simulation(object):

    _SYNC_POINT_UPPER_BOUND = 1000

    def __init__(self, grid) -> None:
        self._grid = copy.deepcopy(grid)
        self._row_length = len(self._grid[0])
        self._flash_count = 0


    @property
    def flash_count(self) -> int:
        return self._flash_count


    def _flash(self, x, y) -> None:
        if self._grid[x][y] == 0:
            return
        
        self._flash_count += 1

        self._grid[x][y] = 0
        offsets = (-1, 0, 1)

        for x_offset in offsets:
            curr_x = x + x_offset
            # out of bounds
            if curr_x < 0 or curr_x >= len(self._grid):
                continue

            for y_offset in offsets:
                curr_y = y + y_offset
                # out of bounds
                if curr_y < 0 or curr_y >= self._row_length:
                    continue

                # it's this one
                if x == curr_x and y == curr_y:
                    continue

                neighbor = self._grid[curr_x][curr_y]
                if neighbor != 0:
                    neighbor += 1

                self._grid[curr_x][curr_y] = neighbor

                if neighbor > 9:
                    self._flash(curr_x, curr_y)


    def simulate_step(self) -> None:
        for x in range(len(self._grid)):
            for y in range(self._row_length):
                self._grid[x][y] += 1

        for x in range(len(self._grid)):
            for y in range(self._row_length):
                val = self._grid[x][y]
                if val > 9:
                    self._flash(x, y)


    def find_sync_point(self) -> int:
        i = 0
        while i < self._SYNC_POINT_UPPER_BOUND:
            i += 1
            self.simulate_step()
            if self._check_all_flashed():
                return i


    def _check_all_flashed(self) -> bool:
        for x in range(len(self._grid)):
            for y in range(self._row_length):
                if self._grid[x][y] != 0:
                    return False
        return True


    def simulate(self, step_count) -> None:
        for _ in range(step_count):
            self.simulate_step()


    def output_grid(self) -> None:
        for line in self._grid:
            print(line)
        print("-" * 25)


simu = Simulation(lines)

simu.simulate(steps)
simu.output_grid()

print("Flash count:", simu.flash_count)


simu = Simulation(lines)

print(simu.find_sync_point())
