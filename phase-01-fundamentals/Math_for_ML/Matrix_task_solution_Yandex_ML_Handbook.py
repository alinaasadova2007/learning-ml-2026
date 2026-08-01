from statistics import pstdev


def matrix_type_check():
    """
    Задание A. Определение типа матрицы.
    Определяет, является ли входная матрица диагональной,
    верхнетреугольной, нижнетреугольной.
    """
    n = int(input())
    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    if all([matrix[i][j] == 0
            for i in range(n) for j in range(n) if i != j]):
        print('DIAGONAL')

    elif all([matrix[i][j] == 0 for
             i in range(n) for j in range(n) if i < j]):
        print('LOWER_TRIANGULAR')

    elif all([matrix[i][j] == 0
             for i in range(n) for j in range(n) if i > j]):
        print('UPPER_TRIANGULAR')

    else:
        print('OTHER')


def matrix_multiplication():
    """
    Задание B. Реализация умножения матриц вручную.
    Вычисляет матрицу C = AB, если данная операция возможна.
    """
    m, n = map(int, input().split())
    matrix_A = []

    for _ in range(m):
        matrix_A.append(list(map(int, input().split())))

    h, k = map(int, input().split())
    matrix_B = []

    for _ in range(h):
        matrix_B.append(list(map(int, input().split())))

    # Проверка на совместимость матриц
    if n != h:
        print('NOT_DEFINED')

    else:
        matrix_C = [[0 for _ in range(k)] for _ in range(m)]
        for r in range(m):
            for c in range(k):
                matrix_C[r][c] = sum([matrix_A[r][i] * matrix_B[i][c]
                                      for i in range(n)])

        for r in range(m):
            print(' '.join(map(str, matrix_C[r])))


def nilpotent_matrix():
    """
    Задание C. Нильпотентные матрицы.
    Вычисляет наименьшее натуральное число k, такое что A^k = 0.
    """
    def matrix_mul(matrix_A: list, matrix_B: list) -> list:
        """
        Вспомогательная функция, вычисляющая произведение двух матриц n*n.
        """
        n = len(matrix)
        new_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_matrix[i][j] = sum([matrix_A[i][k] * matrix_B[k][j]
                                        for k in range(n)])
        return new_matrix

    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    matrix_degree = matrix
    k = 1
    while not all([matrix[i][j] == 0 for i in range(n) for j in range(n)]):
        k += 1
        matrix = matrix_mul(matrix_degree, matrix)

    print(k)


def transpose_matrix():
    """
    Задание E. Реализация транспонирования матрицы вручную.
    Транспонирует входную матрицу m*n.
    """
    m, n = map(int, input().split())
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().split())))

    matrix_transpose = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            matrix_transpose[i][j] = matrix[j][i]

    for row in range(n):
        print(' '.join(map(str, matrix_transpose[row])))


def normalization_of_matrix_columns():
    """
    Задание E. Нормализация столбцов матрицы.
    Нормализует каждый столбец матрицы A следующим образом:

    - Вычитает из каждого элемента столбца среднее значение этого столбца.
    - Делит полученный результат на стандартное отклонение столбца
    - Приводит полученное число к целому, отбрасывая дробную часть
    """
    def transose(matrix: list, m: int, n: int) -> list:
        """
        Вспомогательная функция, транспонирующая матрицу m * n
        """
        transpose_matrix = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                transpose_matrix[i][j] = matrix[j][i]

        return transpose_matrix

    m, n = map(int, input().split())
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().split())))

    new_matrix = transose(matrix, m, n)
    for row in range(n):
        mean = sum(new_matrix[row]) / m
        std = pstdev(new_matrix[row])
        new_matrix[row] = [int((c - mean) / std) for c in new_matrix[row]]

    matrix = transose(new_matrix, n, m)

    for i in range(m):
        print(' '.join(map(str, matrix[i])))
