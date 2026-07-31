import math


def task_a_linear_combination_of_vectors():
    """
    Задание A. Линейная комбинация векторов.
    Умножает векторы на заданные скаляры и находит их сумму.
    """
    k = int(input())
    scalars = list(map(float, input().split()))

    vectors = []
    for i in range(k):
        # Считываем вектор и сразу умножаем каждый его элемент на скаляр
        vector = list(map(float, input().split()))
        vectors.append([val * scalars[i] for val in vector])

    result = []
    # Проходимся по столбцам (по координатам) и суммируем их
    for col in range(len(vectors[0])):
        v_n = sum(vector[col] for vector in vectors)
        result.append(v_n)

    print(" ".join(map(str, result)))


def task_b_orthogonality():
    """
    Задание B. Проверка ортогональности.
    Определяет, ортогональны ли два вектора.
    """
    n = int(input())
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))

    scalar_product = sum(u[i] * v[i] for i in range(n))

    if scalar_product == 0:
        print("ORTHOGONAL")
    else:
        print("NON-ORTHOGONAL")


def task_c_cramers_rule():
    """
    Задание C. Линейная комбинация и базис.
    Находит целочисленные коэффициенты разложения вектора по базису
    с использованием метода Крамера (через определители 2x2).
    """
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())

    # Главный и вспомогательные определители
    D = x1 * y2 - x2 * y1
    D1 = x3 * y2 - x2 * y3
    D2 = x1 * y3 - x3 * y1

    # Проверка на вырожденность и целочисленность решения
    if D != 0 and D1 % D == 0 and D2 % D == 0:
        print(f"{D1 // D} {D2 // D}")
    else:
        print("NO_SOLUTION")


def task_d_angle_between_vectors():
    """
    Задание D. Угол между векторами.
    Вычисляет угол между двумя векторами в градусах.
    """
    n = int(input())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))

    def scalar_product(v, u):
        return sum(v[i] * u[i] for i in range(n))

    dot_prod = scalar_product(v1, v2)
    norm_v1 = scalar_product(v1, v1) ** 0.5
    norm_v2 = scalar_product(v2, v2) ** 0.5

    # Вычисляем косинус угла
    cos_theta = dot_prod / (norm_v1 * norm_v2)
    # Защита от погрешностей вычислений float)
    cos_theta = max(min(cos_theta, 1.0), -1.0)

    result = int(math.degrees(math.acos(cos_theta)))
    print(result)


def task_e_linear_dependence():
    """
    Задание E. Проверка линейной зависимости векторов.
    Определяет линейную зависимость путем приведения матрицы векторов
    к ступенчатому виду (Метод Гаусса) без использования дробей.
    """
    m, n = map(int, input().split())
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().split())))

    # Быстрая проверка: если векторов больше, чем размерность пространства,
    # они гарантированно зависимы
    if m > n:
        print("LINEARLY_DEPENDENT")
        return

    row = 0
    col = 0

    while row < m and col < n:
        # Поиск опорного элемента (пивота)
        for r in range(row, m):
            if matrix[r][col] != 0:
                matrix[row], matrix[r] = matrix[r], matrix[row]
                break

        # Если весь столбец ниже состоит из нулей, переходим к следующему
        if matrix[row][col] == 0:
            col += 1
            continue

        pivot = matrix[row][col]

        # Обнуление элементов под пивотом
        for i in range(row + 1, m):
            target = matrix[i][col]
            for j in range(n):
                matrix[i][j] = matrix[i][j] * pivot - matrix[row][j] * target

        row += 1
        col += 1

    if row == m:
        print("LINEARLY_INDEPENDENT")
    else:
        print("LINEARLY_DEPENDENT")
