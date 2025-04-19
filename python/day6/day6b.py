from tqdm import tqdm

with open("day6_input_sample.txt", "r") as f:
    data = f.read()


class InfiniteLoop(Exception):
    """ Custom Exception for Infinite Loops """
    pass


class Node:
    def __init__(self, char):
        self.char = char
        self.struck = ""

    def __repr__(self):
        return str(self.char)

    def __str__(self):
        return str(self.char)

    def get_struck(self):
        return self.struck

    def set_struck(self, direction: ""):
        if direction not in ["<", "^", ">", "v"]:
            raise Exception("Unhandled guard direction detected")

        if self.char != "#":
            return

        match direction:
            case "<":
                self.struck = "EAST"
            case "^":
                self.struck = "SOUTH"
            case ">":
                self.struck = "WEST"
            case "v":
                self.struck = "NORTH"

        return self.struck


class Guard:
    def __init__(self, index: tuple, direction: str):
        self.index = index
        self.guard_direction = direction

    def cycle_guard_direction(self):
        match self.guard_direction:
            case "<":
                self.guard_direction = "^"
            case "^":
                self.guard_direction = ">"
            case ">":
                self.guard_direction = "v"
            case "v":
                self.guard_direction = "<"


class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix
        self.guard = None
        self.locate_guard()
        self.infinite_loop = False

    def locate_guard(self):
        # Locates the guard in the matrix data
        for i, row in enumerate(self.matrix):  # Y coordinate
            for j, node in enumerate(row):  # X coordinate
                if node.char in ["<", "^", ">", "v"]:
                    self.guard = Guard((j, i), node.char)
                    return
        raise Exception("Guard was not found")

    def check_for_out_of_bounds(self, index: tuple) -> bool:
        x_coord = index[0]
        y_coord = index[1]
        if x_coord < 0 or x_coord > len(self.matrix[0]) - 1:
            return True
        elif y_coord < 0 or y_coord > len(self.matrix) - 1:
            return True
        return False

    def check_for_pivot(self, index: tuple) -> bool:
        x_coord = index[0]
        y_coord = index[1]
        node: Node = self.matrix[y_coord][x_coord]
        if node.char == "#":
            struck_state = node.get_struck()
            new_state = node.set_struck(self.guard.guard_direction)

            if struck_state == new_state:
                raise InfiniteLoop("Whoo-wee Rick I think we are in an infinite loop...")

            return True
        return False

    def move_guard(self) -> bool | str:
        guard_index = self.guard.index
        index = None

        match self.guard.guard_direction:
            case "<":
                # Get target coordinates
                x_coord = self.guard.index[0] - 1
                y_coord = guard_index[1]
                index = (x_coord, y_coord)

            case "^":
                # Get target coordinates
                x_coord = guard_index[0]
                y_coord = guard_index[1] - 1
                index = (x_coord, y_coord)

            case ">":
                # Get target coordinates
                x_coord = guard_index[0] + 1
                y_coord = guard_index[1]
                index = (x_coord, y_coord)

            case "v":
                # Get target coordinates
                x_coord = guard_index[0]
                y_coord = guard_index[1] + 1
                index = (x_coord, y_coord)

        # Check for board exit
        if self.check_for_out_of_bounds(index):
            return False

        # Check for pivot space
        try:
            if self.check_for_pivot(index):
                self.guard.cycle_guard_direction()
                return True

        except InfiniteLoop:
            self.infinite_loop = True
            return False

        # Mark matrix and move guard
        self.guard.index = index
        return True


if __name__ == "__main__":
    with open("day6_input.txt", "r") as f:
        data = f.read()
        rows = data.splitlines()
        matrix_map = [[Node(char) for char in row] for row in rows]

    loops = 0
    loop_matrices = []
    nodes = [node for row in matrix_map for node in row]
    for node in tqdm(nodes):
        original_char = node.char
        if node.char not in ["<", "^", ">", "v"]:
            node.char = "#"
            matrix = Matrix(matrix_map)
            while matrix.move_guard():
                pass
            if matrix.infinite_loop:
                loops += 1

            node.char = original_char

            for nd in nodes:
                nd.struck = False

    print(loops)
