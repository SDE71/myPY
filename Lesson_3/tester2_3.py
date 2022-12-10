courses = ['History', 'Math', 'Programming', 'Literature', 'Physics', 'Math']
numbers = [1, 6, 4, 7, 9, 11]

courses.remove('Math')
# удаляет только одно значение
print(courses)
courses.remove('Math')
# удаляет ещё одно значение
print(courses)
# можно удалить через присвоенный индекс к Math
courses2 = ['History', 'Programming', 'Literature', 'Physics', 'Math']
courses2.remove(courses2[4])
print(courses2)
# срез из списка при таком методе НЕ подойдёт - будет ошибка
# КАК сохранить удалённое? так в этом случае пропадает информация
courses = ['History', 'Math', 'Programming', 'Literature', 'Physics']
# смотрим что происходит при удалении - НИЧЕГО не сохраняется
deleted = courses.remove('Math')
print(deleted)
print(courses)
# как сохранить? Используем метод pop. В этом случае вместо значения запрашивается индекс,
# но сохраняется значение того, что удалили
courses = ['History', 'Math', 'Programming', 'Literature', 'Physics']
deleted = courses.pop(1)
print(deleted)
print(courses)
# при этом при удалении индекса, остальные справа значения уменьшают индекс на 1, т.е. смещаются влево
print(courses[3])
# можно применять и просто метод pop,  в этом случае всё равно сохраняется удалённое значение
courses = ['History', 'Math', 'Programming', 'Literature', 'Physics']
courses.pop(1)
print(courses.pop(1))
print(courses)
# метод pop может работать и без каких-либо аргументов, - забирается последний индекс в списке элементов
courses.pop()
print(courses)
print(courses.pop())
# метод развернуть индексы в оборатном порядке - revirse
courses = ['History', 'Math', 'Programming', 'Literature', 'Physics']
numbers = [1, 6, 4, 7, 9, 11]
print(courses)
courses.reverse()
print(courses)
# вариант из строк тоже применить можно для разворачивания индексов в строке
courses = ['History', 'Math', 'Programming', 'Literature', 'Physics']
numbers = [1, 6, 4, 7, 9, 11]
courses = courses[:: -1]
print(courses)
# можно использовать reversed, но объект сохранятеся как итеррированный объект
# (дальше обсудим) разницу между итерратором и итеррируемым объектом
courses = ['History', 'Math', 'Programming', 'Literature', 'Physics']
numbers = [1, 6, 4, 7, 9, 11]
courses = reversed(courses)
print(courses)
# можно сортировать по уникоду в алфавитном порядке и слова и цифры
courses = ['History', 'Math', 'Programming', 'Literature', 'Physics']
numbers = [1, 13, 6, 4, 7, 9, 11]

print(courses)
courses.sort()
print(courses)

print(numbers)
numbers.sort()
print(numbers)

# Сначала сортируются слова с заглавными буквами, потом со строчными
# если в списке будут цифры, то выдаётся ошибка
courses = ['History', 'history', 'Math', 'Programming', 'Literature', 'Physics']
numbers = [1, 13, 6, 4, 7, 9, 11]

print(courses)
courses.sort()
print(courses)
#  с цифрами всё как в обычной математике
numbers = [1, 13, 6, 4, 7, 9, 11, 0.263, -123]

print(numbers)
numbers.sort()
print(numbers)
# а если нужно использовать в обратном порядке? Добавляем к методу sort (reverse = True)
numbers = [1, 13, 6, 4, 7, 9, 11, 0.263, -123]

print(numbers)
numbers.sort(reverse=True)
print(numbers)
# это же касается и строк
courses = ['History', 'history', 'Math', 'Programming', 'Literature', 'Physics']

print(courses)
courses.sort(reverse=True)
print(courses)

courses = ['History', 'history', 'Math', 'Programming', 'Literature', 'Physics']

print(courses)
print(sorted(courses))

courses = ['History', 'history', 'Math', 'Programming', 'Literature', 'Physics']

print(courses)
print(reversed(courses))
# нужно перевести в список через метод list
print(list(reversed(courses)))
# можно сохранить в новую переменную
sorted_course = sorted(courses)
print(sorted_course)
courses = ['History', 'Math', 'Programming', 'Literature', 'Physics']
numbers = [1, 13, 6, 0.232, -123, 4, 7, 9, 11]

print(min(numbers))
print(max(numbers))

print(min(courses))
print(max(courses))
# в строках с буквами и словами min и max значения ищут по unicod
# в данном случае найдёт минимальное значение "1", а максимальное "history"
courses = ['History', 'Math', 'Programming', 'Literature', 'Physics']
print(min(courses))
print(max(courses))
print(sum(numbers))
# метод sum применим только к цифрам
print(sum(numbers) / len(numbers))

# для строк имеется свой метод поиска индекса
print(courses.index('Physics'))
print(courses[courses.index('Physics')])

course = input('Please enter course name: ')
print(courses.index(course))

# можно найти значение в списках тоже
print('Math' in courses)
# перерыв ( в ролике начало следующего задания в 1 час 18 мин 25 сек.