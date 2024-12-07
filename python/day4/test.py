class Letter:
    def __init__(self, index: tuple, matrix: list):
        self.col, self.row = index
        self.value = matrix[self.row][self.col]
        self.matrix = matrix
        self.xmas_count = 0
        self.build_neighborhood()

    def xmas_check(self, word: str):
        if word == "XMAS":
            self.xmas_count += 1

    def find_east_neighbors(self):
        east_neighbors = self.value
        for i in range(1, 4):
            try:
                neighbor = self.matrix[self.row][self.col + i]
                east_neighbors += neighbor
            except IndexError:
                break
        self.xmas_check(east_neighbors)

    def find_west_neighbors(self):
        west_neighbors = self.value
        for i in range(1, 4):
            try:
                neighbor = self.matrix[self.row][self.col - i]
                west_neighbors += neighbor
            except IndexError:
                break
        self.xmas_check(west_neighbors)

    def find_north_neighbors(self):
        north_neighbors = self.value
        for i in range(1, 4):
            try:
                neighbor = self.matrix[self.row - i][self.col]
                north_neighbors += neighbor
            except IndexError:
                break
        self.xmas_check(north_neighbors)

    def find_south_neighbors(self):
        south_neighbors = self.value
        for i in range(1, 4):
            try:
                neighbor = self.matrix[self.row + i][self.col]
                south_neighbors += neighbor
            except IndexError:
                break
        self.xmas_check(south_neighbors)

    def find_northeast_neighbors(self):
        northeast_neighbors = self.value
        for i in range(1, 4):
            try:
                neighbor = self.matrix[self.row - i][self.col + i]
                northeast_neighbors += neighbor
            except IndexError:
                break
        self.xmas_check(northeast_neighbors)

    def find_northwest_neighbors(self):
        northwest_neighbors = self.value
        for i in range(1, 4):
            try:
                neighbor = self.matrix[self.row - i][self.col - i]
                northwest_neighbors += neighbor
            except IndexError:
                break
        self.xmas_check(northwest_neighbors)

    def find_southeast_neighbors(self):
        southeast_neighbors = self.value
        for i in range(1, 4):
            try:
                neighbor = self.matrix[self.row + i][self.col + i]
                southeast_neighbors += neighbor
            except IndexError:
                break
        self.xmas_check(southeast_neighbors)

    def find_southwest_neighbors(self):
        southwest_neighbors = self.value
        for i in range(1, 4):
            try:
                neighbor = self.matrix[self.row + i][self.col - i]
                southwest_neighbors += neighbor
            except IndexError:
                break
        self.xmas_check(southwest_neighbors)

    def build_neighborhood(self):
        # Cardinal directions
        self.find_east_neighbors()
        self.find_west_neighbors()
        self.find_north_neighbors()
        self.find_south_neighbors()

        # Diagonal directions
        self.find_northeast_neighbors()
        self.find_northwest_neighbors()
        self.find_southeast_neighbors()
        self.find_southwest_neighbors()


with open("day4_input.txt", "r") as f:
    data = f.read()

rows = data.splitlines()
matrix = [[char for char in row] for row in rows]
xmas_found = 0

for row_index, row in enumerate(matrix):
    for column_index, char in enumerate(row):
        index = (column_index, row_index)
        let = Letter(index=index, matrix=matrix)
        xmas_found += let.xmas_count

print(xmas_found)
