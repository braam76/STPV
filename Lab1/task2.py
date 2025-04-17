import math

t = float(input("Введите t: "))
x = float(input("Введите x: "))

numerator = 5 * math.pi * t + 10 * math.cos(x)

denominator = math.sqrt(t) - math.fabs(math.sin(t))

result = (numerator / denominator) * math.exp(x)

print(f"Результат: {result}")
