class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list
        self.len_my_list = len(my_list)
        self.len_my_list_i = len(my_list[0])

    def __str__(self):
        return "\n".join('{}'.format(i) for i in self.my_list)

    def __getitem__(self, item):
        return self.my_list[item]

    def __add__(self, other):
        res_list = []
        if self.len_my_list == other.len_my_list and self.len_my_list_i == other.len_my_list_i:
            for i in range(len(self.my_list)):
                list = []
                for k in range(len(self.my_list[i])):
                    res = self.my_list[i][k] + other[i][k]
                    list.append(res)
                res_list.append(list)
            return res_list
        else:
            return f'Матрицы разного размера'

matrix_1 = Matrix([[1, 5, 7], [8, 9, 4], [3, 8, 1]])
matrix_2 = Matrix([[2, 5, 15], [-1, 23, 0], [4, 7, 125]])
matrix_3 = Matrix([[2, 5, 15, 42], [-1, 23, 0, 14]])
print(matrix_1)
print(matrix_1 + matrix_2)
print(matrix_1 + matrix_3)




