from openpyxl import load_workbook


def check_correct_matrix(matrix: list) -> bool:
    for i in range(len(matrix)):
        if abs(matrix[i][i]) * 2 < sum(list(map(lambda x: abs(x), matrix[i][:-1]))):
            return False
    return True


def solve(matrix: list, pre_x: list):
    global counter, accuracy
    next_x1 = (pre_x[1] * matrix[0][1] + pre_x[2] * matrix[0][2] + pre_x[3] * matrix[0][2] + matrix[0][-1]) / matrix[0][0]
    next_x2 = (pre_x[0] * matrix[1][0] + pre_x[2] * matrix[1][2] + pre_x[3] * matrix[1][3] + matrix[1][-1]) / matrix[1][1]
    next_x3 = (pre_x[0] * matrix[2][0] + pre_x[1] * matrix[2][1] + pre_x[3] * matrix[2][3] + matrix[2][-1]) / matrix[2][2]
    next_x4 = (pre_x[0] * matrix[3][0] + pre_x[1] * matrix[3][1] + pre_x[2] * matrix[3][2] + matrix[3][-1]) / matrix[3][3]
    d1 = abs(pre_x[0] - next_x1)
    d2 = abs(pre_x[1] - next_x2)
    d3 = abs(pre_x[2] - next_x3)
    d4 = abs(pre_x[3] - next_x4)
    table_list.append([counter, pre_x[0], pre_x[1], pre_x[2], pre_x[3], d1, d2, d3, d4])
    counter += 1
    if max(d1, d2, d3, d4) <= accuracy:
        return [matrix]
    else:
        return solve(matrix, pre_x=[next_x1, next_x2, next_x3, next_x4])


if __name__ == "__main__":
    accuracy = float(input("Введите точность вычислений:"))
    file_name_table = "table_of_solve.xlsx"
    table = load_workbook(filename=file_name_table)
    table_list = table['Data']
    table_list.append(['Counter', 'x1', "x2", 'x3', "x4", "d1", "d2", "d3", "d4"])
    counter = 0
    x_lst = [0 for i in range(4)]
    """
    start_matrix = [[28.0, 9.0, -3.0, -7.0, -159.0],
                    [-5.0, 21.0, -5.0, -3.0, 63.0],
                    [-8.0, 1.0, -16.0, 5.0, -45.0],
                    [0.0, -2.0, 5.0, 8.0, 24.0]]
    """
    start_matrix = [[-19.0, 2.0, -1.0, -8.0, -38.0],
                    [-2.0, 14.0, 0.0, -4.0, 20.0],
                    [6.0, -5.0, -20.0, -6.0, -52.0],
                    [-6.0, 4.0, -2.0, 15.0, 43.0]]

    for i in range(len(start_matrix)):
        for j in range(len(start_matrix)):
            if i != j:
                start_matrix[i][j] = -start_matrix[i][j]
    print(x_lst)
    print(f"Статус удовлетворенности матрицы: {check_correct_matrix(start_matrix)}")
    solve(matrix=start_matrix, pre_x=x_lst)
    table.save(file_name_table)
    table.close()
