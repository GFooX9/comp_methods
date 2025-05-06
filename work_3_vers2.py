def f(x):
    """Исходная функция: 0.25x^3 + x - 1.2502"""
    return 0.25 * x ** 3 + x - 1.2502


def df(x):
    """Производная функции: 0.75x^2 + 1"""
    return 0.75 * x ** 2 + 1


def simple_iteration(phi, x0, eps, max_iter=1000):
    """
    Метод простой итерации для решения уравнений x = phi(x)

    Параметры:
    phi - функция итерации
    x0 - начальное приближение
    eps - точность
    max_iter - максимальное число итераций

    Возвращает:
    корень, количество итераций
    """
    x_prev = x0

    for i in range(max_iter):
        x_next = phi(x_prev)

        # Проверка сходимости
        if abs(x_next - x_prev) < eps:
            # Дополнительная проверка, что f(x) близко к 0
            if abs(f(x_next)) < 10 * eps:
                return x_next, i + 1
            else:
                raise ValueError("Итерации сошлись, но f(x) не близко к 0")

        x_prev = x_next

    raise ValueError(f"Метод не сошелся за {max_iter} итераций. Последнее значение: {x_prev}")


def newton(f, df, x0, eps, max_iter=1000):
    """
    Метод Ньютона для решения уравнений f(x) = 0

    Параметры:
    f - исходная функция
    df - производная функции
    x0 - начальное приближение
    eps - точность
    max_iter - максимальное число итераций

    Возвращает:
    корень, количество итераций
    """
    x_prev = x0

    for i in range(max_iter):
        f_val = f(x_prev)
        df_val = df(x_prev)

        # Защита от деления на ноль
        if abs(df_val) < 1e-12:
            raise ValueError(f"Производная близка к нулю в точке {x_prev}")

        x_next = x_prev - f_val / df_val

        # Проверка сходимости
        if abs(x_next - x_prev) < eps:
            # Проверка, что f(x) действительно близко к 0
            if abs(f(x_next)) < 10 * eps:
                return x_next, i + 1
            else:
                raise ValueError("Итерации сошлись, но f(x) не близко к 0")

        x_prev = x_next

    raise ValueError(f"Метод не сошелся за {max_iter} итераций. Последнее значение: {x_prev}")


def check_convergence(phi, a, b, n_points=100):
    """
    Проверяет условие сходимости |phi'(x)| < 1 на [a,b]
    Использует численное дифференцирование
    """
    h = (b - a) / n_points
    max_derivative = 0

    for i in range(n_points + 1):
        x = a + i * h
        # Численная производная
        dx = 1e-5
        phi_prime = (phi(x + dx) - phi(x)) / dx
        current_deriv = abs(phi_prime)
        if current_deriv > max_derivative:
            max_derivative = current_deriv

    if max_derivative >= 1:
        print(f"Внимание: |phi'| = {max_derivative:.4f} >= 1, сходимость не гарантирована")
    else:
        print(f"Условие сходимости выполняется: |phi'| = {max_derivative:.4f} < 1")


# Основные вычисления
if __name__ == "__main__":
    # Метод простой итерации
    phi = lambda x: (5.0008 - 4 * x) ** (1 / 3)
    x0_simple = 1.0
    eps = 0.0001

    # Проверка сходимости (численный метод)
    print("Проверка сходимости метода простой итерации:")
    check_convergence(phi, 0, 2)

    try:
        root_simple, iter_simple = simple_iteration(phi, x0_simple, eps)
        print(f"\nМетод простой итерации:")
        print(f"Корень: x = {root_simple:.6f}")
        print(f"f(x) = {f(root_simple):.6e}")
        print(f"Итераций: {iter_simple}")
    except Exception as e:
        print(f"\nОшибка в методе простой итерации: {e}")

    # Метод Ньютона
    x0_newton = 1.0

    try:
        root_newton, iter_newton = newton(f, df, x0_newton, eps)
        print(f"\nМетод Ньютона:")
        print(f"Корень: x = {root_newton:.6f}")
        print(f"f(x) = {f(root_newton):.6e}")
        print(f"Итераций: {iter_newton}")
    except Exception as e:
        print(f"\nОшибка в методе Ньютона: {e}")