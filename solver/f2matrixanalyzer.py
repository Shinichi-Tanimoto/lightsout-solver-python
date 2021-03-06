#coding: utf-8

import f2

class F2MatrixAnalyzer:

    def __init__(self, array, size):
        if len(array) != size * size:
            raise Exception("引数のサイズの整合性が合いません。")
        self.__left_cells = [[f2.F2(array[size * i + j]) for j in range(size)] for i in range(size)]
        self.__right_cells = [[f2.F2(0) for j in range(size)] for i in range(size)]
        for i in range(size):
            self.__right_cells[i][i] = f2.F2(1)
        self.__size = size
        self.__unsolvables = []
        self.__is_analized = False

    def __str__(self):
        left = "left [%s]" % ",".join(["[%s]" % ','.join([str(cell) for cell in row]) for row in self.__left_cells])
        right = "right [%s]" % ",".join(["[%s]" % ','.join([str(cell) for cell in row]) for row in self.__right_cells])
        return left + "\n" + right

    def __swap_row(self, i0, i1):
        temp = self.__left_cells[i0]
        self.__left_cells[i0] = self.__left_cells[i1]
        self.__left_cells[i1] = temp

        temp = self.__right_cells[i0]
        self.__right_cells[i0] = self.__right_cells[i1]
        self.__right_cells[i1] = temp

    def __sub_row(self, index0, index1):
        self.__left_cells[index1] = [ x1 - x0 for x1, x0 in zip(self.__left_cells[index1], self.__left_cells[index0])]
        self.__right_cells[index1] = [ x1 - x0 for x1, x0 in zip(self.__right_cells[index1], self.__right_cells[index0])]

    def __pivot(self, index):
        if self.__left_cells[index][index] == f2.F2(1):
            return True
        for i in range(index, self.__size):
            if self.__left_cells[i][index] == f2.F2(1):
                self.__swap_row(i, index)
                return True
        return False

    def analyze(self):
        if self.__is_analized:
            return

        "左側行列を上三角行列にする"
        for i in range(self.__size):
            if self.__pivot(i):
                for k in range(i + 1, self.__size):
                    if self.__left_cells[k][i] == f2.F2(1):
                        self.__sub_row(i, k)
            else:
                self.__unsolvables.append(i)

        "左側行列を単位行列にしていく"
        for i in range(self.__size):
            target_i = self.__size - 1 - i
            if self.__left_cells[target_i][target_i] == f2.F2(1):
                for k in range(i + 1, self.__size):
                    target_k = self.__size - 1 - k
                    if self.__left_cells[target_k][target_i] == f2.F2(1):
                        self.__sub_row(target_i, target_k)

        self.__is_analized = True
        return

    def is_analyzed(self):
        return self.__is_analized

    def has_inverse(self):
        if not self.__is_analized:
            return False
        return len(self.__unsolvables) == 0

    def get_inverse(self):
        if not self.__is_analized:
            return None
        elif self.has_inverse():
            return self.__right_cells
        else:
            return None

    def __prod_vec(self, f2_vector):
        result = [ f2.F2(0) for i in range(self.__size) ]
        for i in range(self.__size):
            for k in range(self.__size):
                result[i] += self.__right_cells[i][k] * f2_vector[k]
        return result

    def in_image(self, array):
        if not self.__is_analized:
            return False
        elif len(array) != self.__size:
            return False

        f2_vector = [f2.F2(i) for i in array]
        f2_vector2 = self.__prod_vec(f2_vector);
        for i in self.__unsolvables:
            if f2_vector2[i] == f2.F2(1):
                return False
        return True

    def get_coimage_list(self, array):
        if not self.__is_analized:
            return False
        elif len(array) != self.__size:
            return False

        f2_vector = [f2.F2(i) for i in array]
        f2_vector2 = self.__prod_vec(f2_vector);
        for i in self.__unsolvables:
            if f2_vector2[i] == f2.F2(1):
                return []

        sets = self.__get_kernel_vectors()
        for i in range(len(sets)):
            sets[i] = sets[i] + f2_vector2
        return sets


    def __get_kernel_vectors(self):
        if len(self.__unsolvables) == 0:
            return [[f2.F2(0) for i in range(self.__size)]]

        kernel_base_vectors = []
        """ 基底ベクトルの計算 """
        for i in self.__unsolvables:
            v = [f2.F2(0) for i in range(self.__size)]
            for j in range(0, i - 1):
                if self.__left_cells[j][i] == f2.F2(1):
                    v[j] = f2.F2(1)
            v[i] = f2.F2(1)
            kernel_base_vectors.append(v)

        """ 基底ベクトルからの計算 """
        sets = [[f2.F2(0) for i in range(self.__size)]]
        for v in kernel_base_vectors:
            sets_temp = []
            for s in sets:
                sets_temp.append(s + v)
                sets_temp.append(s)
            sets = sets_temp
        return sets








if __name__ == '__main__':
    analyzer = F2MatrixAnalyzer([1, 1, 1, 1, 0, 1, 1, 0, 1], 3)
    print analyzer
    print analyzer.analyze()
    print analyzer
    print analyzer.has_inverse()
    print analyzer.in_image([0, 0, 1])
