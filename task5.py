# Дано ціле число, яке лежить в діапазоні 1-999. Вивести його рядок опис виду «парне двозначне число», «непарне трьохзначне число» і т. Д.

def find_print(a):
    div2 = False
    signs_amount = 1

    if a < 10:
        signs_amount = 1
    elif 9 < a < 100:
        signs_amount = 2
    elif 99 < a < 999:
        signs_amount = 3

    if (a % 2) == 0:
        div2 = True

    if div2:
        if signs_amount == 1:
            print("парна цифра")
        if signs_amount == 2:
            print("парне двозначне число")
        if signs_amount == 3:
            print("парне трьохзначне число")
    else:
        if signs_amount == 1:
            print("непарна цифра")
        if signs_amount == 2:
            print("непарне двозначне число")
        if signs_amount == 3:
            print("непарне трьохзначне число")


a = int(input("Введіть число від 1 до 999: "))

if a < 1 or a > 999:
    print("Неправильний ввод")
else:
    find_print(a)
