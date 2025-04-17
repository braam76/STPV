from datetime import datetime

def main():
    try:
        # Ввод данных пользователя
        surname = input("Введите фамилию: ").strip()
        name = input("Введите имя: ").strip()
        patronymic = input("Введите отчество: ").strip()
        gender = input("Введите пол (м/ж): ").strip().lower()
        birth_date_str = input("Введите дату рождения (ДД.ММ.ГГГГ): ").strip()
        group = input("Введите группу: ").strip()

        # Проверка пола
        if gender not in ('м', 'ж'):
            raise ValueError("Пол должен быть 'м' или 'ж'")

        # Парсинг даты рождения
        birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y").date()

        today = datetime.today().date()

        # Вычисление возраста
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        # Год поступления — предположим, что студент поступил в 18 лет
        year_admission = birth_date.year + 18

        # Курс — вычисляем по году поступления и текущему году
        course = today.year - year_admission
        if course < 1:
            course = 1  # минимальный курс - 1

        # Формируем инициалы
        initials = f"{name[0].upper()}.{patronymic[0].upper()}."

        # Выбор слов в зависимости от пола
        birth_word = "родился" if gender == 'м' else "родилась"
        admission_word = "поступил" if gender == 'м' else "поступила"

        # Итоговая фраза
        phrase = (
            f"Меня зовут {surname} {initials} "
            f"Я {birth_word} {birth_date.strftime('%d.%m.%Y')}. "
            f"В {year_admission} году я {admission_word} в ДонНТУ. "
            f"Я учусь в группе {group} на {course} курсе. "
            f"Мне исполнилось {age} лет."
        )

        print(phrase)

    except ValueError as ve:
        print(f"Ошибка ввода: {ve}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
