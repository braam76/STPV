from .input_check import *

def _print(apartments, title="Квартиры"):
    print(f"\n{title}:")
    if not apartments:
        print("  Нет подходящих квартир.")
        return
    for i, apt in enumerate(apartments, 1):
        print(f"  {i}. {apt['address']}: {apt['rooms']} комн., этаж {apt['floor']}, "
              f"общая {apt['total_area']} м², жилая {apt['living_area']} м², "
              f"телефон: {'есть' if apt['phone'] else 'нет'}, цена: {apt['price']} руб.")

def _add(apartments):
    try:
        print("\nДобавление новой квартиры:")
        address = with_validation("  Адрес: ", cast_func=str, allow_empty=False)
        rooms = with_validation("  Количество комнат: ", cast_func=int, allow_empty=False)
        total_area = with_validation("  Общая площадь (м²): ", cast_func=float, allow_empty=False)
        living_area = with_validation("  Жилая площадь (м²): ", cast_func=float, allow_empty=False)
        floor = with_validation("  Этаж: ", cast_func=int, allow_empty=False)
        phone = with_validation("  Наличие телефона (да/нет): ", cast_func=str,
                                      allowed_values=['да', 'нет'], allow_empty=False)
        phone = (phone == 'да')
        price = with_validation("  Цена (руб): ", cast_func=float, allow_empty=False)

        new_apt = {
            'rooms': rooms,
            'total_area': total_area,
            'living_area': living_area,
            'floor': floor,
            'phone': phone,
            'price': price,
            'address': address
        }
        apartments.append(new_apt)
        print("Квартира успешно добавлена.")
    except Exception as e:
        print(f"Ошибка при добавлении квартиры: {e}")




def _search(apartments,
                      rooms=None,
                      floor_min=None, floor_max=None,
                      phone=None,
                      living_area_min=None, living_area_max=None,
                      price_max=None,
                      total_area_min=None, total_area_max=None):
    filtered = apartments
    print("\nНачинаем поиск по заданным параметрам...")

    if rooms is not None:
        filtered = [apt for apt in filtered if apt['rooms'] == rooms]
        print(f"Фильтр по количеству комнат = {rooms}: {len(filtered)} квартир")

    if floor_min is not None:
        filtered = [apt for apt in filtered if apt['floor'] >= floor_min]
        print(f"Фильтр по минимальному этажу = {floor_min}: {len(filtered)} квартир")

    if floor_max is not None:
        filtered = [apt for apt in filtered if apt['floor'] <= floor_max]
        print(f"Фильтр по максимальному этажу = {floor_max}: {len(filtered)} квартир")

    if phone is not None:
        filtered = [apt for apt in filtered if apt['phone'] == phone]
        print(f"Фильтр по наличию телефона = {'есть' if phone else 'нет'}: {len(filtered)} квартир")

    if living_area_min is not None:
        filtered = [apt for apt in filtered if apt['living_area'] >= living_area_min]
        print(f"Фильтр по минимальной жилой площади = {living_area_min} м²: {len(filtered)} квартир")

    if living_area_max is not None:
        filtered = [apt for apt in filtered if apt['living_area'] <= living_area_max]
        print(f"Фильтр по максимальной жилой площади = {living_area_max} м²: {len(filtered)} квартир")

    if price_max is not None:
        filtered = [apt for apt in filtered if apt['price'] <= price_max]
        print(f"Фильтр по максимальной цене = {price_max} руб.: {len(filtered)} квартир")

    if total_area_min is not None:
        filtered = [apt for apt in filtered if apt['total_area'] >= total_area_min]
        print(f"Фильтр по минимальной общей площади = {total_area_min} м²: {len(filtered)} квартир")

    if total_area_max is not None:
        filtered = [apt for apt in filtered if apt['total_area'] <= total_area_max]
        print(f"Фильтр по максимальной общей площади = {total_area_max} м²: {len(filtered)} квартир")

    return filtered
