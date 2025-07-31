import itertools
import operator


class Equation:
    def __init__(self):
        self.solution = 0
        self.nums = []
        self.ops = []
        self.equations = []
        self.countable = False

    def __str__(self):
        return f"Equation(Solution: {self.solution}, Nums: {self.nums}, Ops: {self.ops}, Eqtns: {self.equations}, Ctb: {self.countable})"

    def __repr__(self):
        return f"Equation(Solution: {self.solution}, Nums: {self.nums}, Ops: {self.ops}, Eqtns: {self.equations}, Ctb: {self.countable})"

    def build(self, data: str):
        split_colon = data.split(":")
        self.solution = int(split_colon[0])
        self.nums = [int(num) for num in split_colon[1].split(" ") if num not in ["", " "]]

        self._set_ops()
        self._build_equations()
        self._evaluate_equations()

        return self

    def _set_ops(self):
        operator_slots = len(self.nums) - 1
        op_master = [op for op in itertools.product("+*|", repeat=operator_slots)]
        self.ops = op_master

    def _build_equations(self):
        for op in self.ops:
            self.equations.append([val for pair in zip(self.nums, op + ("",)) for val in pair][:-1])

    def _evaluate_equations(self):
        def combine(a: int, b: int) -> int:
            return int(str(a) + str(b))

        op_map = {
            "+": operator.add,
            "*": operator.mul,
            "|": combine,
        }

        for equation in self.equations:
            val = equation.pop(0)

            while equation:
                char = equation.pop(0)
                val = op_map[char](val, equation.pop(0))

            if val == self.solution:
                self.countable = True

def read_file() -> list:
    with open("day7a_input.txt", "r") as f:
        data = [j.strip() for j in f.readlines()]
    return data


if __name__ == "__main__":
    df = read_file()
    equations = [Equation().build(line) for line in df]
    total = 0
    for eqt in equations:
        if eqt.countable:
            total += eqt.solution
    print(total)
