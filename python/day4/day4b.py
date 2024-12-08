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
        self.northeast_neighbor = ""
        self.northwest_neighbor = ""
        self.southeast_neighbor = ""
        self.southwest_neighbor = ""


    def find_northeast_neighbor(self):
        try:
            if self.row-1 < 0:
                self.northeast_neighbor = "."
                return

            neighbor = self.matrix[self.row - 1][self.col + 1]
            self.northeast_neighbor = neighbor

        except IndexError:
            pass

    def find_northwest_neighbor(self):
        try:
            if self.row-1 < 0 or self.col-1 < 0:
                self.northwest_neighbor = "."
                return

            neighbor = self.matrix[self.row - 1][self.col - 1]
            self.northwest_neighbor = neighbor

        except IndexError:
            pass

    def find_southeast_neighbor(self):
        try:
            neighbor = self.matrix[self.row + 1][self.col + 1]
            self.southeast_neighbor = neighbor

        except IndexError:
            pass

    def find_southwest_neighbor(self):
        try:
            if self.col-1 < 0:
                self.southwest_neighbor = "."
                return

            neighbor = self.matrix[self.row + 1][self.col - 1]
            self.southwest_neighbor += neighbor

        except IndexError:
            pass

    def build_neighborhood(self):
        # Diagonals
        self.find_northeast_neighbor()
        self.find_northwest_neighbor()
        self.find_southeast_neighbor()
        self.find_southwest_neighbor()

    def check_xmas(self):
        count = 0

        if self.northwest_neighbor + self.value + self.southeast_neighbor in ["MAS", "SAM"]:
            if self.northeast_neighbor + self.value + self.southwest_neighbor in ["MAS", "SAM"]:
                count += 1

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

        if char != "A":
            continue

        let = Letter(index=index, matrix=matrix)
        let.build_neighborhood()
        xmas_found += let.check_xmas()

print(xmas_found)
