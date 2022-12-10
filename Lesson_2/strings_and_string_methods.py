string_sample = "Hello world world"
string_sample_1 = "Hello world world world"
# прямая индексация работает с нуля 0123456
# обратная индексация работает -5, -4, -3, -2, -1
string_sample2 = "first letteR is lowErcase"
string_sample2_1 = "first letteR is lowErcase. Hello worlf"
string_sample3 = " extra whitespace string "
string_sample3_1 = "   *    extra whitespace string     *  "
string_sample3_2 = "*****extra whitespace string***"
german_sample = "der Fluß"
prosto_sample = "der Flu₸"
print(len(string_sample))

print(string_sample[0:4])
# при прямой индексации последний символ не учитывается, нужно брать на 1 шаг больше
print(string_sample[0:5])
# индексация в квадратных скобках есть некий старт и финиши и шаг [start:end:step]
print(string_sample[-1])
print(string_sample[-5:-1])
# как обойти проблемму, чтобы показать букву d? Надо не указывать после двоеточий
print(string_sample[-5:])
# также можно сделать и в прямой индексации
print(string_sample[:10])
# вырезать внутри строки можно указать
print(string_sample[10:])
# при обратной индексации нужно брать не учитывая ноль
print(string_sample[-17])
# попробуем вырезать из строки в середине слово world
print(string_sample[6:11])
print(string_sample)
string_sample777 = string_sample[6:11]
print(string_sample777)
# учимся применять шаг 2
print(string_sample[0:11:2])
# учимся применять шаг 3
print(string_sample[0:11:3])
# строка наоборот через обратный индекс и не указываем старт и финиш, а только шаг минус 1
print(string_sample[::-1])
string_sample777 = string_sample[4:15]
print(string_sample777)
print(string_sample777[::-1])
print(string_sample777[::-2])
# с числами работать нельзя - нужно перевести в строку
print(len('123456789'))
# проверка подстроки внутри другой строки
print("world" in string_sample)
print("planet" in string_sample)
print(string_sample in string_sample)
print(string_sample in "Hello world world")
# команда IN осуществляет проверку на присутствие подстроки в строке

print("A" == "a")
# двойное равно - проверка на равенство регистров
# Hello hello HELLO чтобы Python различал и находил равенство слов при разном регистре букв

print(string_sample2)
print(type(len("Hello world")))
# можно через точку выводить другие методы
print(string_sample2.upper())
# команда upper поднимает всё в верхний регистр
# теперь приведём в нижний регистр 2 методами
# первый метод команда lower
print(german_sample.lower())
# второй метод команда casefold переводит други символы в латинские символы
print(german_sample.casefold())
print(prosto_sample.lower())
# Третий метод все буквы прописные, а первая буква должна быть заглавной - метод capitalize
print(string_sample2.capitalize())
# метод capitalize делает в строке только первую букву заглавной
# этот метод нужен когда вводятся данные от пользователя - для предотвращения ошибки ввода
print(string_sample2_1.capitalize())
user_name = 'roMan'
print(user_name.capitalize())
# можно сразу присвоить вводу правильное писание
user_name = user_name.capitalize()
print(user_name)

# у метода print есть возможность доп свойств - пока print делает на разных строках
print("Hello")
print("world")
# добавим метод end и две строки объединяться в одну строку
print("Hello", end='***')
print("world")

# метод strip позволяет добавлять или удалять любое количество символов, например пробелы
print(string_sample3.strip())
# но если вместе с пробелами будут другие символы, то пробелы будут удалены только до символов
print(string_sample3_1.strip())
# добавив артгументы, можно удалить символы те, которые указаны
print(string_sample3_2.strip("*"))
# удаление слева символов - команда lstrip
print(string_sample3_2.lstrip('*'))
# удаление справа символов - команда rstrip
print(string_sample3_2.rstrip('*'))
# метод replace может менять текущее (старое) слово или букву на новое
print(string_sample.replace('world', 'planet'))
print(string_sample.replace('w', ''))
print(string_sample.replace(' w', ''))
# можно указать сколько раз поменять
print(string_sample.replace('world', 'planet', 1))
# через точку можно добавлять разные методы подряд
# power (перевести в нижний регистр), strip (вырезать что-то), и заменить что-то на что-то
# испольнение идёт от ближайшего слева метода и далее вправо
print(string_sample_1.lower().strip('h').replace('world', 'planet', 2))
# метод считает сколько полных слов или букв
print(string_sample_1.count('world'))
# если указать период в регистрах, то будет искать в этих пределах
print(string_sample_1.count('world', 10, 18))
# другой метод find ищет только первое совпадение
print(string_sample_1.find('world'))
# цифра 6 - это номер регистра
print(string_sample_1.find('world', 7, 18))
