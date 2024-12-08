"""
OK HOLY SHIT IF YOU EVER CREATE A NEGATIVE INDEX YOU NEED TO UNDERSTAND THAT THAT IS APPLICABLE IN INDEXING
WHERE YOU DON'T EXPECT IT. GOD.

I handled out of bounds indexes using a try|except block on IndexError, however negative indexes will not
raise IndexError as they will then point towards the element enumerated from the end of the iterable. This
is fine for out of bounds positive integers, but not negative integers. I've known this for years, yet it
still slipped through.

Also, just use numpy
"""


class Letter:
    def __init__(self, index: tuple, matrix: list):
        self.col, self.row = index
        self.value = matrix[self.row][self.col]
        self.matrix = matrix
        self.east_neighbors = self.value
        self.west_neighbors = self.value
        self.north_neighbors = self.value
        self.south_neighbors = self.value
        self.northeast_neighbors = self.value
        self.northwest_neighbors = self.value
        self.southeast_neighbors = self.value
        self.southwest_neighbors = self.value

    def find_east_neighbors(self):
        for i in range(1, 4):
            try:
                neighbor = self.matrix[self.row][self.col + i]
                self.east_neighbors += neighbor
            except IndexError:
                break

    def find_west_neighbors(self):
        for i in range(1, 4):
            try:
                if self.col-i < 0:
                    self.west_neighbors = "Nope"
                    break

                neighbor = self.matrix[self.row][self.col - i]
                self.west_neighbors += neighbor
            except IndexError:
                break

    def find_north_neighbors(self):
        for i in range(1, 4):
            try:
                if self.row-i < 0:
                    self.north_neighbors = "Nope"
                    break

                neighbor = self.matrix[self.row - i][self.col]
                self.north_neighbors += neighbor
            except IndexError:
                break

    def find_south_neighbors(self):
        for i in range(1, 4):
            try:
                neighbor = self.matrix[self.row + i][self.col]
                self.south_neighbors += neighbor
            except IndexError:
                break

    def find_northeast_neighbors(self):
        for i in range(1, 4):
            try:
                if self.row-i < 0:
                    self.northeast_neighbors = "Nope"
                    break

                neighbor = self.matrix[self.row - i][self.col + i]
                self.northeast_neighbors += neighbor
            except IndexError:
                break

    def find_northwest_neighbors(self):
        for i in range(1, 4):
            try:
                if self.row-i < 0 or self.col-i < 0:
                    self.northwest_neighbors = "Nope"
                    break

                neighbor = self.matrix[self.row - i][self.col - i]
                self.northwest_neighbors += neighbor
            except IndexError:
                break

    def find_southeast_neighbors(self):
        for i in range(1, 4):
            try:
                neighbor = self.matrix[self.row + i][self.col + i]
                self.southeast_neighbors += neighbor
            except IndexError:
                break

    def find_southwest_neighbors(self):
        for i in range(1, 4):
            try:
                if self.col-i < 0:
                    self.southwest_neighbors = "Nope"
                    break

                neighbor = self.matrix[self.row + i][self.col - i]
                self.southwest_neighbors += neighbor
            except IndexError:
                break

    def build_neighborhood(self):
        # Cardinal
        self.find_east_neighbors()
        self.find_west_neighbors()
        self.find_north_neighbors()
        self.find_south_neighbors()

        # Diagonals
        self.find_northeast_neighbors()
        self.find_northwest_neighbors()
        self.find_southeast_neighbors()
        self.find_southwest_neighbors()

    def check_xmas(self):
        count = 0
        direct_map = {
            "east": self.east_neighbors,
            "west": self.west_neighbors,
            "north": self.north_neighbors,
            "south": self.south_neighbors,
            "ne": self.northeast_neighbors,
            "nw": self.northwest_neighbors,
            "se": self.southeast_neighbors,
            "sw": self.southwest_neighbors
        }
        for k, v in direct_map.items():
            if v == "XMAS":
                count += 1
                # print(f"XMAS found at {self.row}, {self.col} in the {k} direction")

        return count


with open("day4_input.txt", "r") as f:
    data = f.read()

rows = data.splitlines()
matrix = [[char for char in row] for row in rows]
xmas_found = 0
letters = []

for row_index, row in enumerate(matrix):
    for column_index, char in enumerate(row):
        index = (column_index, row_index)

        if char != "X":
            continue

        let = Letter(index=index, matrix=matrix)
        let.build_neighborhood()
        xmas_found += let.check_xmas()

print(xmas_found)
# 2557