def task_a_critical_points() -> None:
    '''
    Задание A. Нахождение экстремумов функции на заданном интервале.
    Находит критические точки полинома третьей степени аналитическим методом
    и определяет их характер с помощью второй производной.
    '''
    a, b, c, d_coeff = map(float, input().split())
    p, q = map(float, input().split())

    def func(x: float) -> float:
        return a * x ** 3 + b * x ** 2 + c * x + d_coeff

    def second_derivative(x: float) -> float:
        return 6.0 * a * x + 2.0 * b

    def find_roots() -> set[float]:
        roots: set[float] = set()
        if a != 0.0:
            discriminant: float = (2.0 * b) ** 2 - 12.0 * a * c
            if discriminant < 0.0:
                return roots
            else:
                x_1: float = (-2.0 * b + discriminant ** 0.5) / (6.0 * a)
                x_2: float = (-2.0 * b - discriminant ** 0.5) / (6.0 * a)
                roots.add(x_1)
                roots.add(x_2)
        else:
            if b != 0.0:
                x: float = -c / (2.0 * b)
                roots.add(x)
        return roots

    roots: set[float] = find_roots()
    valid_roots: list[float] = [x for x in roots if p <= x <= q]

    if not valid_roots:
        print('No critical points found.')
    else:
        valid_roots.sort()
        for x in valid_roots:
            if abs(second_derivative(x)) < 1e-6:
                print(f'Saddle point at x = {x:.5f}')
                print(f'f(x) = {func(x):.5f}')

            elif second_derivative(x) > 0.0:
                print(f'Local minimum at x = {x:.5f}')
                print(f'f(x) = {func(x):.5f}')

            elif second_derivative(x) < 0.0:
                print(f'Local maximum at x = {x:.5f}')
                print(f'f(x) = {func(x):.5f}')


def task_b_newtons_method() -> None:
    '''
    Задание B. Метод Ньютона.
    Находит корень квадратного уравнения с помощью численного метода Ньютона,
    используя приближенное вычисление производной.
    '''
    a, b, c = map(float, input().split())
    x_0: float = float(input())
    epsilon: float = float(input())

    def func(x: float) -> float:
        return a * x ** 2 + b * x + c

    def deriv(x: float) -> float:
        h: float = 1e-5
        return (func(x + h) - func(x)) / h

    no_solution: bool = True
    iteration: int = 0
    x_n: float = x_0

    if abs(func(x_0)) < epsilon:
        no_solution = False
    else:
        for i in range(1, 1001):
            derivative_val: float = deriv(x_n)
            if derivative_val != 0.0:
                x_n = x_n - (func(x_n) / derivative_val)
                if abs(func(x_n)) < epsilon:
                    no_solution = False
                    iteration = i
                    break
            else:
                break

    if no_solution:
        print('Solution not found')
    else:
        print(f'Root found: x = {x_n:.6f}')
        print(f'Number of iterations: {iteration}')
