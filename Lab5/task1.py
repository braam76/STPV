from helpers import input_check
from helpers import apartments
from helpers import file_operations

def main():
    apts = [
        {
            'rooms': 3,
            'total_area': 75.0,
            'living_area': 45.0,
            'floor': 5,
            'phone': True,
            'price': 5500000,
            'address': 'ул. Ленина, д.10, кв.15'
        },
        {
            'rooms': 2,
            'total_area': 50.0,
            'living_area': 30.0,
            'floor': 3,
            'phone': False,
            'price': 3500000,
            'address': 'пр. Мира, д.5, кв.8'
        },
        {
            'rooms': 4,
            'total_area': 90.0,
            'living_area': 60.0,
            'floor': 7,
            'phone': True,
            'price': 7500000,
            'address': 'ул. Пушкина, д.20, кв.3'
        }
    ]

    while True:
        print("\nМеню:")
        print("1. Показать все квартиры")
        print("2. Добавить новую квартиру вручную")
        print("3. Добавить квартиры из файла")
        print("4. Сохранить квартиры в файл")
        print("5. Поиск квартир")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ").strip()
        if choice == '1':  # печать всех квартир
            apartments._print(apts, "Все квартиры")
        elif choice == '2':  # загрузка из ввода 
            apartments._add(apts)
        elif choice == '3':  # загрузить из файла
            file_operations.load_from_file(apts)
        elif choice == '4':  # сохранение в файл
            file_operations.save_to_file(apts)
        elif choice == '5':  # поиск квартир
            params = input_check.search_parameters()
            filtered = apartments._search(apts, **params)
            apartments._print(filtered, "Результаты поиска")
            if filtered:
                prices = [apt['price'] for apt in filtered]
                print(f"\nМинимальная цена среди найденных квартир: {min(prices)} руб.")
                print(f"Максимальная цена среди найденных квартир: {max(prices)} руб.")
        elif choice == '6':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
