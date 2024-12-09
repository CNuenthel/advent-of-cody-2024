from pprint import pprint

with open("day6_input_sample.txt", "r") as f:
    data = f.read()

rows = data.splitlines()
matrix = [[char for char in row] for row in rows]

class GuardMonitor:
    def __init__(self, floor_matrix: list):
        self.matrix = floor_matrix
        self.guard_index = (0, 0)
        self.guard_direction = None

    def locate_guard(self):
        # Locates the guard in the matrix data
        for i, row in enumerate(self.matrix):  # Y coordinate
            for j, char in enumerate(row):  # X coordinate
                if char in ["<", "^", ">", "v"]:
                    self.guard_index = (j, i)
                    self.guard_direction = char

    def set_guard_direction(self):
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

    def move_guard(self):
        # Move guard in currently set guard_direction
        # self.matrix[y][x]
        step_off_index = self.guard_index
        match self.guard_direction:
            case "<":
                if step_off_index[1]-1 >= 0:
                    step_to_index = (step_off_index[0], step_off_index[1]-1)
                