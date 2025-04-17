import random
from pprint import pprint

def generate_random_list(length, start=1, end=None):
    """
    Генерирует список случайных целых чисел длины length.
    Диапазон чисел: [start, end) (end не включается).
    Если end не задан, то end = length.
    """
    if end is None:
        end = length
    return [random.randrange(start, end) for _ in range(length)]

def print_list(lst, title="Список"):
    """
    Выводит список с заголовком.
    """
    print(f"{title}: {lst}")

def print_matrix(matrix, title="Матрица"):
    """
    Выводит матрицу с заголовком, используя pprint для удобства.
    """
    print(f"\n{title}:")
    pprint(matrix)

def find_min_abs_element(matrix):
    """
    Находит минимальный по модулю элемент в матрице и его позицию.
    Возвращает кортеж (min_value, (row_index, col_index))
    """
    min_val = None
    min_pos = (0, 0)
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if min_val is None or abs(val) < abs(min_val):
                min_val = val
                min_pos = (i, j)
    return min_val, min_pos

def remove_row_and_col(matrix, row_to_remove, col_to_remove):
    """
    Возвращает новую матрицу без указанной строки и столбца.
    """
    return [
        [val for j, val in enumerate(row) if j != col_to_remove]
        for i, row in enumerate(matrix) if i != row_to_remove
    ]

def check_input(_input, _condition, _error=""):
    """
    Проверяет ввод и возвращает значение из ввода.
    """
    while True:
        try:
            tmp = _input()
            if not _condition(tmp):
                raise ValueError(_error)
            return tmp
        
        except KeyboardInterrupt:
            print("\nВвод прерван пользователем.")
        except Exception as e:
            print(f"ERROR: {_error} ({e})")