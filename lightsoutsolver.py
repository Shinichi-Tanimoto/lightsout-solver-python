#coding: utf-8

from solver import f2matrixanalyzer

def __put_value_as_matrix(array, size, i, j, value):
    array[i * size + j] = value


def solve_lightsout(lights, size):
    array = [ 0 for i in range(size * size * size * size)]

    "タップ操作行列作成"
    for i in range(size):
        for j in range(size):
            target = i * size + j
            __put_value_as_matrix(array, size * size, target, target, 1)
            if i > 0:
                __put_value_as_matrix(array, size * size, target, (i - 1) * size + j, 1)
            if i < size - 1:
                __put_value_as_matrix(array, size * size, target, (i + 1) * size + j, 1)
            if j > 0:
                __put_value_as_matrix(array, size * size, target, i * size + j - 1, 1)
            if j < size - 1:
                __put_value_as_matrix(array, size * size, target, i * size + j + 1, 1)

    "行列分析"
    analyzer = f2matrixanalyzer.F2MatrixAnalyzer(array=array, size=size * size)
    analyzer.analyze()

    print analyzer
    "タップ操作行列が任意の行列でとくことができるか"
    print analyzer.has_inverse()

    "このライツアウトが解けるかどうか"
    print analyzer.in_image(lights)

    "解ける場合最小の解を探る"
    print analyzer.get_coimage_list(lights)



if __name__ == '__main__':
    solve_lightsout([1,0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], 4)
