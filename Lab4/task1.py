from helpers import input_check
from helpers import apartments

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
        print("2. Добавить квартиру")
        print("3. Поиск квартир")
        print("4. Выход")

        choice = input("Выберите действие (1-4): ").strip()
        if choice == '1':
            apartments._print(apts, "Все квартиры")
        elif choice == '2':
            apartments._add(apts)
        elif choice == '3':
            params = input_check.search_parameters()
            filtered = apartments._search(apts, **params)
            apartments._print(filtered, "Результаты поиска")
            if filtered:
                prices = [apt['price'] for apt in filtered]
                print(f"\nМинимальная цена среди найденных квартир: {min(prices)} руб.")
                print(f"Максимальная цена среди найденных квартир: {max(prices)} руб.")
        elif choice == '4':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
