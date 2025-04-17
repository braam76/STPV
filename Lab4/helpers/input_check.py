def with_validation(prompt, cast_func=None, allowed_values=None, allow_empty=True):
    """
    Универсальная функция ввода с проверкой.

    :param prompt: сообщение для ввода
    :param cast_func: функция преобразования (например, int, float), None — без преобразования (строка)
    :param allowed_values: список допустимых значений (после преобразования), None — любые
    :param allow_empty: разрешить пустой ввод (возвращает None)
    :return: преобразованное значение или None, если пустой ввод разрешён
    """
    while True:
        val = input(prompt).strip()
        if allow_empty and val == '':
            return None
        try:
            v = cast_func(val) if cast_func else val
        except ValueError:
            print("Неверный формат ввода. Попробуйте ещё раз.")
            continue
        if allowed_values is not None and v not in allowed_values:
            allowed_str = ', '.join(str(x) for x in allowed_values)
            print(f"Допустимые значения: {allowed_str}. Попробуйте ещё раз.")
            continue
        return v


def search_parameters():
    print("\nВведите параметры поиска. Чтобы пропустить параметр, просто нажмите Enter.")
    rooms = with_validation("Количество комнат: ", cast_func=int)
    floor_min = with_validation("Минимальный этаж: ", cast_func=int)
    floor_max = with_validation("Максимальный этаж: ", cast_func=int)
    phone = with_validation("Наличие телефона (да/нет): ", cast_func=str,
                                  allowed_values=['да', 'нет'], allow_empty=True)
    if phone is not None:
        phone = (phone == 'да')
    living_area_min = with_validation("Минимальная жилая площадь (м²): ", cast_func=float)
    living_area_max = with_validation("Максимальная жилая площадь (м²): ", cast_func=float)
    price_max = with_validation("Максимальная цена (руб): ", cast_func=float)
    total_area_min = with_validation("Минимальная общая площадь (м²): ", cast_func=float)
    total_area_max = with_validation("Максимальная общая площадь (м²): ", cast_func=float)

    return {
        'rooms': rooms,
        'floor_min': floor_min,
        'floor_max': floor_max,
        'phone': phone,
        'living_area_min': living_area_min,
        'living_area_max': living_area_max,
        'price_max': price_max,
        'total_area_min': total_area_min,
        'total_area_max': total_area_max
    }

