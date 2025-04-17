import random
from pprint import pprint
from list_utils import print_matrix, find_min_abs_element, remove_row_and_col, check_input

size = check_input(
    lambda: int(input("Введите размер квадратной матрицы (целое положительное число): ")),
    lambda x: x > 0,
    "Размер должен быть положительным числом"
)

print("Выберите способ заполнения матрицы (1, 2 или 3): ")
print("1. Случайным образом")
print("2. С клавиатуры")
print("3. По формуле A[i][j] = a*i + b/i - c*j")

choice = check_input(
    lambda: int(input("Ввод: ")),
    lambda x: x in [1, 2, 3],
    "Выберите 1, 2 или 3"
)

matrix = []

match choice:
    case 1:
        matrix = [[random.uniform(0, 100) for _ in range(size)] for _ in range(size)]
    case 2:
        print(f"Введите элементы матрицы размером {size}x{size}:")
        for i in range(size):
            row = []
            for j in range(size):
                val = check_input(
                    lambda: float(input(f"A[{i}][{j}] = ")),
                    lambda x: True,
                    "Введите корректное число"
                )
                row.append(val)
            matrix.append(row)
    case 3:
        print("Введите коэффициенты a, b, c (числа):")
        a = check_input(lambda: float(input("a = ")), lambda x: True)
        b = check_input(lambda: float(input("b = ")), lambda x: True)
        c = check_input(lambda: float(input("c = ")), lambda x: True)
        for i in range(1, size+1):
            row = []
            for j in range(1, size+1):
                val = a*i + b/i - c*j
                row.append(val)
            matrix.append(row)

print_matrix(matrix, "Исходная матрица")

min_val, (row_to_remove, col_to_remove) = find_min_abs_element(matrix)
print(f"\nМинимальный по модулю элемент: {min_val} на позиции {(row_to_remove, col_to_remove)}")

new_matrix = remove_row_and_col(matrix, row_to_remove, col_to_remove)

print_matrix(new_matrix, "Матрица после удаления строки и столбца с минимальным элементом")
