"""
Вычислить интеграл a/b(f(x)dx с помощью формулы
1)Ньютона-Лейбница
2)Приближенно формуле прямоугольников
*Отрезок интегрирования разбить с шагом 10
*Все вычисления проводить, сохраняя не менее 4 знаков после запятой
*Приближенное значение интеграла округлить до 3-го десятичного знака
*Найти абсолютную и относительную погрешность результата вычислений

Вариант 4

a = 1
b = 4
f(x) = (x^3+2)/x^5

"""


# функция
def func(x) -> float:
    # return pow(x, (3 / 2))
    return (pow(x, 3) + 2) / pow(x, 5)


# первообразная
def primitive(x):
    # return 2 * pow(x, 2.5) / 5
    return -1 * (2 * pow(x, 3) + 1) / (2 * pow(x, 4))


if __name__ == "__main__":
    a = int(input("Left line: "))
    b = int(input("Right line: "))
    count = 10
    h = ((b - a) / count)
    lst = []
    for i in range(count):
        value = a + h * i
        lst.append(round(value, 2))
    lst.append(b)
    print(lst)
    I1 = h * sum(list(map(lambda x: func(x), lst[1:])))
    I2 = h * sum(list(map(lambda x: func(x), lst[:-1])))
    I = (I1 + I2) / 2
    newton = primitive(b) - primitive(a)
    absolute_error = round(abs(I - newton), 3)
    relative_error = round(absolute_error / I * 100, 3)
    print(f"I1 = {round(I1, 4)}")
    print(f"I2 = {round(I2, 4)}")
    print(f"I = {round(I, 4)}")
    print(f"Newton = {round(newton, 4)}")
    print(f"Absolute error = {absolute_error}")
    print(f"Absolute error = {relative_error}%")
