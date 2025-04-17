import os
from .input_check import with_validation

def parse_bool(text):
    text = text.strip().lower()
    if text in ('да', 'yes', 'true', '1'):
        return True
    elif text in ('нет', 'no', 'false', '0'):
        return False
    else:
        raise ValueError(f"Неверное булево значение: {text}")

def load_from_file(apartments):
    filename = os.path.abspath(input("Введите имя файла для загрузки (например, apartments.txt): ").strip())
    print(filename)
    if not os.path.isfile(filename):
        print("Файл не найден.")
        return
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        current_apt = {}
        count_loaded = 0
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.lower().startswith('квартира'):
                if current_apt:
                    apartments.append(current_apt)
                    count_loaded += 1
                    current_apt = {}
                continue
            if ':' not in line:
                continue
            key, val = map(str.strip, line.split(':', 1))
            key_lower = key.lower()
            try:
                if key_lower == 'адрес':
                    current_apt['address'] = val
                elif key_lower == 'количество комнат':
                    current_apt['rooms'] = int(val)
                elif key_lower == 'общая площадь':
                    current_apt['total_area'] = float(val)
                elif key_lower == 'жилая площадь':
                    current_apt['living_area'] = float(val)
                elif key_lower == 'этаж':
                    current_apt['floor'] = int(val)
                elif key_lower == 'телефон':
                    current_apt['phone'] = parse_bool(val)
                elif key_lower == 'цена':
                    current_apt['price'] = float(val)
            except Exception as e:
                print(f"Ошибка при разборе строки '{line}': {e}")

        # Добавляем последнюю квартиру, если есть
        if current_apt:
            apartments.append(current_apt)
            count_loaded += 1

        # Запросить, сколько записей использовать (если нужно)
        count = with_validation(f"Загружено {count_loaded} квартир. Сколько использовать? (Enter — все): ", cast_func=int, allow_empty=True)
        if count is not None and count < count_loaded:
            # Оставим только первые count квартир
            del apartments[count:]
        print(f"Загружено {len(apartments)} квартир из файла '{filename}'.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

def save_to_file(apartments):
    if not apartments:
        print("Нет данных для сохранения.")
        return
    filename = input("Введите имя файла для сохранения (например, output.txt): ").strip()
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for i, apt in enumerate(apartments, 1):
                f.write(f"квартира {i}\n")
                f.write(f"Адрес: {apt.get('address', '')}\n")
                f.write(f"Количество комнат: {apt.get('rooms', '')}\n")
                f.write(f"Общая площадь: {apt.get('total_area', '')}\n")
                f.write(f"Жилая площадь: {apt.get('living_area', '')}\n")
                f.write(f"Этаж: {apt.get('floor', '')}\n")
                f.write(f"Телефон: {'да' if apt.get('phone', False) else 'нет'}\n")
                f.write(f"Цена: {apt.get('price', '')}\n\n")
        print(f"Данные успешно сохранены в файл '{filename}'.")
    except Exception as e:
        print(f"Ошибка при записи файла: {e}")
