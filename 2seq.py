punctuation = [',', '/', ';']
inp = input("Введите любые числа через запятую, слэш или точку с запятой:")
punctuation.remove(inp[1])
for punc in punctuation:
    if punc in inp:
        print("Вы использовали несколько разделителей! Надо выбрать лишь один знак в качестве разделителя!")
        break
else:
    list = inp.split(inp[1])
    final_list = []
    for num in list:
        if list.count(num) == 1:
            final_list.append(num)
    print("Результат:", ", ".join(sorted(final_list)))