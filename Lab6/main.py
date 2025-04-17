import tkinter as tk
from tkinter import ttk

# Функция для конвертации между десятичной и двоичной системами
def convert_number():
    try:
        value = entry_value.get().strip()
        from_system = combo_from.get()
        to_system = combo_to.get()

        if from_system == to_system:
            # Если системы совпадают, просто выводим введённое значение
            result.set(value)
            return

        if from_system == "Десятичная":
            # Конвертация из десятичной в двоичную
            decimal_number = int(value)
            converted = bin(decimal_number)[2:]  # убираем '0b'
        else:
            # Конвертация из двоичной в десятичную
            # Проверяем, что введено корректное двоичное число
            if not all(ch in '01' for ch in value):
                raise ValueError("Некорректное двоичное число")
            converted = str(int(value, 2))

        result.set(converted)
    except ValueError:
        result.set("Ошибка ввода!")

# Функция очистки полей
def clear_fields():
    entry_value.delete(0, tk.END)
    result.set("")

# Создание главного окна
root = tk.Tk()
root.title("Конвертер систем счисления")
root.geometry("350x200")
root.resizable(False, False)

# Стилизация
style = ttk.Style()
style.configure("TButton", padding=5, font=("Arial", 10))
style.configure("TLabel", font=("Arial", 10))
style.configure("TCombobox", padding=5, font=("Arial", 10))

# Виджеты
frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

ttk.Label(frame, text="Введите число:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_value = ttk.Entry(frame, font=("Arial", 10))
entry_value.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Из системы:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
combo_from = ttk.Combobox(frame, values=["Десятичная", "Двоичная"], state="readonly")
combo_from.grid(row=1, column=1, padx=5, pady=5)
combo_from.current(0)

ttk.Label(frame, text="В систему:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
combo_to = ttk.Combobox(frame, values=["Десятичная", "Двоичная"], state="readonly")
combo_to.grid(row=2, column=1, padx=5, pady=5)
combo_to.current(1)

result = tk.StringVar()
label_result = ttk.Label(frame, textvariable=result, font=("Arial", 12, "bold"), foreground="blue")
label_result.grid(row=3, column=0, columnspan=2, pady=10)

btn_convert = ttk.Button(frame, text="Конвертировать", command=convert_number)
btn_convert.grid(row=4, column=0, columnspan=2, pady=5)

btn_clear = ttk.Button(frame, text="Очистить", command=clear_fields)
btn_clear.grid(row=5, column=0, columnspan=2, pady=5)

# Запуск цикла
root.mainloop()
