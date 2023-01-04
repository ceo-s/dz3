list = input("Введите любые числа для списка №1 исключительно через запятую(без пробелов):").split(",")
list2 = input("Введите любые числа для списка №2 исключительно через запятую(без пробелов):").split(",")

result = []

for elem in list:
    if elem not in list2:
        result.append(elem)

print("Результат:", ", ".join(result))