class Vector:
    """
    Класс для представления математического вектора и операций над ним.
    """

    def __init__(self, coords: list[float]) -> None:
        """
        Инициализирует вектор.

        Аргументы:
            coords: Список координат вектора.
        """
        self.coords = coords

    def __str__(self) -> str:
        """
        Возвращает строковое представление вектора.
        """
        return f"Вектор с координатами: {self.coords}"

    def __add__(self, other: Vector) -> Vector:
        """
        Складывает два вектора поэлементно.

        Аргументы:
            other: Вектор для сложения.

        Возвращает:
            Новый вектор, являющийся суммой исходных.

        Исключения:
            ValueError: Если длины векторов не совпадают.
        """
        if len(self.coords) != len(other.coords):
            raise ValueError("Попытка сложить векторы разной длины")
        return Vector([a + b for a, b in zip(self.coords, other.coords)])

    def __mul__(self, other: Vector) -> float:
        """
        Вычисляет скалярное произведение двух векторов.

        Аргументы:
            other: Вектор для умножения.

        Возвращает:
            Результат скалярного произведения.

        Исключения:
            ValueError: Если длины векторов не совпадают.
        """
        if len(self.coords) != len(other.coords):
            raise ValueError("Попытка умножить векторы разной длины")
        return sum(a * b for a, b in zip(self.coords, other.coords))

    def __abs__(self) -> float:
        """
        Вычисляет евклидову норму вектора.

        Возвращает:
            Длину вектора.
        """
        return (self * self) ** 0.5


if __name__ == "__main__":
    # Создание векторов
    v1 = Vector([1.0, 2.0, 3.0])
    v2 = Vector([4.0, 5.0, 6.0])

    print("Созданы векторы:")
    print(f"v1 = {v1}")
    print(f"v2 = {v2}\n")

    # Сложение векторов
    v3 = v1 + v2
    print(f"Результат сложения (v1 + v2): {v3}\n")

    # Скалярное произведение
    dot_product = v1 * v2
    print(f"Скалярное произведение (v1 * v2): {dot_product}\n")

    # Вычисление нормы (длины)
    v4 = Vector([3.0, 4.0])  # Египетский треугольник, норма должна быть 5.0
    print(f"v4 = {v4}")
    print(f"Норма (длина) вектора v4: {abs(v4)}\n")

    # Проверка защиты от ошибок
    print("Проверка защиты от сложения векторов разной длины:")
    try:
        invalid_sum = v1 + v4
    except ValueError as e:
        print(f"Успешно поймана ошибка: {e}")
