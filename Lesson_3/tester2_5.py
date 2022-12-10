# Изучаем кортеж (TUPLE)
courses = ['History', 'Math', 'Programming', 'Literature', 'Physics']
numbers = [1, 13, 6, 0.232, -123, 4, 7, 9, 11]

# вспоминаем - в списке мы можем индексировать элемент и заменить его
courses[1] = 'Hello world'
print(courses)
# заменяем [] на (), т.е. из спсика создаём кортеж
courses = ('History', 'Math', 'Programming', 'Literature', 'Physics')
# мы объявляем кортеж либо круглыми скобками либо объявив метод tuple
# при чём этот жем метод является методом конвертации (строку в кортеж),
# а используя метод list конвертируем кортеж в список
empty_tuple = ()
empty_tuple2 = tuple()

print(numbers)
print(tuple(numbers))

print(courses)
print(list(courses))

print(courses[2])
# в кортеже мы не можем взять какой-нибудь элемент, взять и заменить его, как в списке
# для замены элемента мы кортеж сначала превращаем в список
courses = list(courses)
print(courses)
courses[2] = 'Hello world'
print(courses)
courses = tuple(courses)
print(courses)
# в кортеже могут применять методы
# index (вызвать индекс элемента и показать что за элемент стоит в этом индексе)
# count считает количество появление какого-то элемента
print(courses.index('Literature'))
print(courses.count('Literature'))
# единственный способ изменить кортеж не конвертируя его - это сложить кортеж с ещё одним кортежем
new_tuple = (1, 2, 3)
print(courses + new_tuple)
# если у нас есть много данных и нам надо подавать в виде какого-то сложного объекта
# (несколько данных в одной переменной), то используется кортеж.
# Если работаем с изменяемыми данными, то работаем со списком
