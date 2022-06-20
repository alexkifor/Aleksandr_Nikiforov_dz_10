class Cell():
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num > other.num:
            return self.num - other.num
        else:
            return f'метод невыполним'

    def __mul__(self, other):
        return self.num * other.num

    def __floordiv__(self, other):
        if other.num > 0:
            return self.num // other.num
        else:
            return f'метод невыполним'

    def __truediv__(self, other):
        if other.num > 0:
            return self.num / other.num
        else:
            return f'метод невыполним'

    def make_order(self, n):
        list_1 = []
        list = []
        for i in range(1, self.num + 1):
            list.append('*')
        for i in range(0, len(list), n):
            each_chunk = list[i:n + i]
            list_1.append(''.join(each_chunk))
        return (('\ n '.join(list_1))).replace(' ', '')


cell_1 = Cell(18)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(4))

