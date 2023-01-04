import random

TOLSTOY = {"name": "Лев Толстой", "age": "09.09.1828"} 
BALE = {"name": "Кристиан Бейл", "age": "30.01.1974"}
KNYAZ = {"name": "Князь Владимир (только год)", "age": "14.04.958"}
MIAMOTO = {"name": "Миямото Мусаси", "age": "19.06.1584"}
TYSON = {"name": "Майк Тайсон", "age": "30.06.1966"}
LENIN = {"name": "Владимир Ильич Ленин", "age": "22.04.1870"}
MIURA = {"name": "Кентаро Миура", "age": "11.07.1966"}
CYPLENKOV = {"name": "Денис Цыпленков", "age": "10.03.1982"}
BANDI = {"name": "Тэд Банди", "age": "24.11.1946"}
INSTASAMKA = {"name": "Инстасамка", "age": "11.06.2000"}


LIST = [TOLSTOY, BALE, KNYAZ, MIAMOTO, TYSON, LENIN, MIURA, CYPLENKOV, BANDI, INSTASAMKA]

day_dict = dict(zip(["09","10","11","14","19","22","24","30"], ["Девятого", "Десятого", "Одинатцатого", "Четырнатцатого", "Девятнатцатого", "Двадцать второго", "Двадцать четвертого", "Тритцатого"]))
month_dict = dict(zip(["01", "03", "04", "06", "07", "09", "11"], ["января", "марта", "апреля", "июня", "июля", "сентября", "ноября"]))

list = random.sample(LIST, 5)
counter = 0
polling = True 

while polling == True:
    for person in list:
        answer = input(f"Напиши дату рождения для {person['name']} в формате dd.mm.yyyy :")
        if str(person["age"]) == answer:
            print("Молодец!")
            counter += 1
        else:
            print(f"Не совсем, правильный ответ - {day_dict[person['age'].split('.')[0]]} {month_dict[person['age'].split('.')[1]]} {person['age'].split('.')[-1]}")
    print("Викторина пройдена. Ваш рейтинг:", f"{counter}/{len(list)}  ({len(list)-counter} ошибок)", f"Процент правильных ответов - {counter/len(list)*100}%. Неправильных - {100 - counter/len(list)*100}%")
    answer = input("Хотите пройти викторину заново? ДА/НЕТ:")
    if answer == "ДА":
        counter = 0
    else:
        print("До новых встреч!")
        polling = False