import math


def task_a_sequence_element() -> None:
    '''
    Задание A. Вычисление элемента последовательности.
    Рассчитывает значение a_n = n / (n + 1) и выводит его с точностью 6 знаков.
    '''
    n: int = int(input())
    a_n: float = n / (n + 1)
    print(f'{a_n:.6f}')


def task_b_function_continuity() -> None:
    '''
    Задание B. Проверка непрерывности функции в точке.
    Использует левый и правый пределы с заданным допуском epsilon.
    '''
    func: str = input()
    x_0: float = float(input())
    delta: float = float(input())
    epsilon: float = 5.0 * delta

    val_center: float = float(eval(func, {}, {'x': x_0}))
    val_left: float = float(eval(func, {}, {'x': x_0 - delta}))
    val_right: float = float(eval(func, {}, {'x': x_0 + delta}))

    first_condition: bool = abs(val_left - val_center) < epsilon
    second_condition: bool = abs(val_right - val_center) < epsilon

    if first_condition and second_condition:
        print('CONTINUOUS')
    else:
        print('DISCONTINUOUS')


def task_c_lipschitz_continuity() -> None:
    '''
    Задание C. Условие Липшица.
    Проверяет, является ли функция Липшицевой непрерывной на интервале.
    '''
    epsilon: float = 1e-6
    func_expr: str = input()
    a, b = map(float, input().split())
    e: float = math.e
    const_l: float = float(eval(input()))

    func = eval('lambda x, e=e: ' + func_expr)

    steps: int = 10000
    step_size: float = (b - a) / steps
    condition: bool = True

    for i in range(steps):
        x_1: float = a + i * step_size
        x_2: float = a + (i + 1) * step_size

        if abs(func(x_1) - func(x_2)) > const_l * abs(x_1 - x_2) + epsilon:
            condition = False
            break

    if condition:
        print('LIPSCHITZ')
    else:
        print('NOT LIPSCHITZ')


if __name__ == '__main__':
    task_c_lipschitz_continuity()
