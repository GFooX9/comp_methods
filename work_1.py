import numpy as np


def gauss_Func(matrix):
    # функция меняет матрицу через побочные эффекты
    # если вам нужно сохранить прежнюю матрицу, скопируйте её np.copy
    for nrow, row in enumerate(matrix):
        # nrow равен номеру строки
        # row содержит саму строку матрицы
        divider = row[nrow]  # диагональный элемент
        # делим на диагональный элемент.
        row /= divider
        # теперь надо вычесть приведённую строку из всех нижележащих строчек
        for lower_row in matrix[nrow + 1:]:
            factor = lower_row[nrow]  # элемент строки в колонке nrow
            lower_row -= factor * row  # вычитаем, чтобы получить ноль в колонке nrow
    # все строки матрицы изменились, в принципе, можно и не возвращать
    return matrix


def make_identity(matrix):
    # перебор строк в обратном порядке
    for nrow in range(len(matrix) - 1, 0, -1):
        row = matrix[nrow]
        for upper_row in matrix[:nrow]:
            factor = upper_row[nrow]
            upper_row -= factor * row
    return matrix


def condition_output(matrix, result_matrix):
    size_first_axis = len(matrix)
    size_second_axis = len(matrix[1]) - 1
    print("\n\tНачальная система уравнений ВАРИАНТА № 4:")
    for i in range(size_first_axis):
        for j in range(size_second_axis):
            if j != size_second_axis - 1:
                print(f"({matrix[i][j]})x{j + 1} + ", end="")
            else:
                print(f"({matrix[i][j]})x{j + 1} ", end="")
        print(f"= {matrix[i][-1]}")
    print("\n\tПолученный результат ВАРИАНТА № 4:")
    for i in range(size_first_axis):
        print(f"x{i + 1}:", end=" ")
        for j in range(size_second_axis):
            print(f"{result_matrix[i][j]} ", end=" ")
        print(f" |{int(result_matrix[i][-1])}")


if __name__ == "__main__":
    start_matrix = np.array([[26.0, -9.0, -8.0, 8.0, 20.0],
                             [9.0, -21.0, -2.0, 8.0, -164.0],
                             [-3.0, 2.0, -18.0, 8.0, 140.0],
                             [1.0, -6.0, -1.0, 11.0, -81.0]])
    next_matrix = start_matrix.copy()
    result = make_identity(gauss_Func(next_matrix))
    condition_output(matrix=start_matrix, result_matrix=result)
