# Дано три цілих числа: A, B, C. Перевірити істинність висловлювання: «Число B знаходиться між числами A і C».

a, b, c = map(int, input("Введіть А, В, С: ").split())

if a < b and b < c:
    print("Число В знаходиться між числами А та С")
