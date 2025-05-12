"""
Решить задачу Коши для обыкновенного дифференциального уравнения
первого порядка y' = f(x, y), удовлетворяющего условиям y(x0) = y0
на отрезке [0;1], шаг h = 0.1 методом Рунге-Кута. Все вычисления вести
с 4 десятичными знаками.
y' = (1-y^2)*cos(x) + 0.6*y__________________y(0) = 0.
"""
import math


# Функция правой части ODU
def f(x, y):
    return 1 - pow(y, 2) * math.cos(x) + 0.6 * y


def output(answer_x: list, answer_y: list, count: int):
    for i in range(count):
        print(f"Value x{i} = {answer_x[i]}, Value y(x{i}) = {round(answer_y[i], 4)}")


def runge_kutta(start_poz, end_poz, count, step_h):
    # создание массива x_i
    lst_x = [round(start_poz + i * h, 1) for i in range(count)]
    print(lst_x)
    lst_y = [start_poz]
    for i in range(count):
        k1 = step_h * f(lst_x[i], lst_y[i])
        k2 = step_h * f(lst_x[i] + step_h / 2, lst_y[i] + k1 / 2)
        k3 = step_h * f(lst_x[i] + step_h / 2, lst_y[i] + k2 / 2)
        k4 = step_h * f(lst_x[i] + step_h, lst_y[i] + k3)

        yi_1 = lst_y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        lst_y.append(yi_1)

    output(answer_x=lst_x, answer_y=lst_y, count=count)
    return 1


if __name__ == "__main__":
    a = 0  # y(a) = 0
    b = 1
    h = 0.1
    N = int((b - a) / h)
    runge_kutta(start_poz=a, end_poz=b, count=N+1, step_h=h)
