with open("day6_input_sample.txt", "r") as f:
    data = f.read()

rows = data.splitlines()
matrix = [[char for char in row] for row in rows]


class GuardMonitor:
    def __init__(self, floor_matrix: list):
        self.matrix = floor_matrix
        self.guard_index = (0, 0)
        self.guard_direction = None
        self.obstructions = []
        self.locate_guard_and_obstructions()

    def locate_guard_and_obstructions(self):
        # Locates the guard in the matrix data
        for i, row in enumerate(self.matrix):  # Y coordinate
            for j, char in enumerate(row):  # X coordinate
                if char in ["<", "^", ">", "v"]:
                    self.guard_index = (j, i)
                    self.guard_direction = char
                elif char == "#":
                    index = [j, i]
                    self.obstructions.append(index)

    def cycle_guard_direction(self):
        x_coord = self.guard_index[0]
        y_coord = self.guard_index[1]

        # Modifies guard direction
        match self.guard_direction:
            case "<":
                self.guard_direction = "^"
            case "^":
                self.guard_direction = ">"
            case ">":
                self.guard_direction = "v"
            case "v":
                self.guard_direction = "<"

        self.matrix[y_coord][x_coord] = self.guard_direction

    def check_for_pivot(self, index: tuple) -> bool:
        x_coord = index[0]
        y_coord = index[1]

        if self.matrix[y_coord][x_coord] == "#":
            # Modify obstruction data with edge struck by guard vector
            obs_index = None
            for i, coord in enumerate(self.obstructions):
                if list(index) == coord[:2]:
                    obs_index = i
                    break

            edge = None
            match self.guard_direction:
                case ">":
                    edge = "|-"
                case "<":
                    edge = "-|"
                case "^":
                    edge = "_|_"
                case "v":
                    edge = "T"

            self.obstructions[obs_index].append(edge)

            return True
        return False

    def check_for_out_of_bounds(self, index: tuple) -> bool:
        x_coord = index[0]
        y_coord = index[1]
        if x_coord < 0 or x_coord > len(self.matrix[0]) - 1:
            return True
        elif y_coord < 0 or y_coord > len(self.matrix) - 1:
            return True
        return False

    def mark_matrix(self, index: tuple):
        x_coord = index[0]
        y_coord = index[1]
        self.matrix[y_coord][x_coord] = "X"

    def move_guard(self) -> bool:
        guard_index = self.guard_index

        match self.guard_direction:
            case "<":
                # Get target coordinates
                x_coord = self.guard_index[0] - 1
                y_coord = guard_index[1]
                index = (x_coord, y_coord)

                # Check for board exit
                if self.check_for_out_of_bounds(index):
                    self.mark_matrix(guard_index)
                    return False

                # Check for pivot space
                if self.check_for_pivot(index):
                    self.cycle_guard_direction()
                    return True

                # Mark matrix and move guard
                self.mark_matrix(guard_index)
                self.matrix[y_coord][x_coord] = self.guard_direction
                self.guard_index = (x_coord, y_coord)
                return True

            case "^":
                # Get target coordinates
                x_coord = guard_index[0]
                y_coord = guard_index[1] - 1
                index = (x_coord, y_coord)

                # Check for board exit
                if self.check_for_out_of_bounds(index):
                    self.mark_matrix(guard_index)
                    return False

                # Check for pivot space
                if self.check_for_pivot(index):
                    self.cycle_guard_direction()
                    return True

                # Mark matrix, move guard, and update guard index
                self.mark_matrix(guard_index)
                self.matrix[y_coord][x_coord] = self.guard_direction
                self.guard_index = (x_coord, y_coord)

                return True

            case ">":
                # Get target coordinates
                x_coord = guard_index[0] + 1
                y_coord = guard_index[1]
                index = (x_coord, y_coord)

                # Check for board exit
                if self.check_for_out_of_bounds(index):
                    self.mark_matrix(guard_index)
                    return False

                # Check for pivot space
                if self.check_for_pivot(index):
                    self.cycle_guard_direction()
                    return True

                # Mark matrix and move guard
                self.mark_matrix(guard_index)
                self.matrix[y_coord][x_coord] = self.guard_direction
                self.guard_index = (x_coord, y_coord)

                return True

            case "v":
                # Get target coordinates
                x_coord = guard_index[0]
                y_coord = guard_index[1] + 1
                index = (x_coord, y_coord)

                # Check for board exit
                if self.check_for_out_of_bounds(index):
                    self.mark_matrix(guard_index)
                    return False

                # Check for pivot space
                if self.check_for_pivot(index):
                    self.cycle_guard_direction()
                    return True

                # Mark matrix and move guard
                self.mark_matrix(guard_index)
                self.matrix[y_coord][x_coord] = self.guard_direction
                self.guard_index = (x_coord, y_coord)

                return True

    def retrace_steps(self):
        count = 0
        for row in self.matrix:
            for step in row:
                if step == "X":
                    count += 1
        print(count)

    def develop_counter_ops(self):
        # What if you just put an obstacle on every location the guard steps on, run the route and see if it infinite
        # loops?
        pass


if __name__ == "__main__":
    gm = GuardMonitor(matrix)

    # Set walking flag
    walking = True

    while walking:
        walking = gm.move_guard()

    gm.retrace_steps()
