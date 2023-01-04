numbers_count = input("Введите количество элементов:")
list = []
for i in range(int(numbers_count)):
    number = input(f"Введите {i+1} элемент:")
    list.append(number)
print("Результат:", ", ".join(sorted(list)))