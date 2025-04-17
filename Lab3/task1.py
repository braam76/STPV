import re

try:
    while True:
        s = input("Введите строку (не пустую): ").strip()
        if s:
            break
        print("Строка не должна быть пустой. Попробуйте снова.")

    matches = re.findall(r'н+', s)
    if matches:
        longest = max(matches, key=len)
        print(f"Самая длинная последовательность 'н': '{longest}', длина: {len(longest)}")
    else:
        print("В строке нет буквы 'н'.")
    
    modified_s = s.replace('.', '!')
    print("Строка после замены точек на '!':")
    print(modified_s)

except KeyboardInterrupt:
    print("\nВвод прерван пользователем.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
