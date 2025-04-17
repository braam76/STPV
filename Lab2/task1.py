from list_utils import generate_random_list, print_list, check_input

m = check_input(
    lambda: int(input("Введите размер квадратной матрицы (целое положительное число): ")),
    lambda x: x > 0,
    "Размер должен быть положительным числом"
)

def task1(m):
    try:
        arr = generate_random_list(m, 1, m)
        print_list(arr, "Список случайных значений")
        SM = (1/m) * sum(arr)
        return SM
    except Exception as e:
        print(f"ERROR: {e}")
        return 0

print(f"Результат расчета: {task1(m)}")
