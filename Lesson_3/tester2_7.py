# давайте разберём -  что такое set (Множество) и поставим финурные скобки
courses1 = ['History', 'Math', 'Programming', 'Literature', 'Physics']
courses = {'History', 'Math', 'Programming', 'Literature', 'Physics'}
numbers = [1, 13, 6, 0.232, -123, 4, 7, 9, 11]
print(type(courses1))
print(type(courses))
# не разрашает дубликаты, невозможно его изменить, не упорядочен, нет порядковых номером, не имеет индексов
# одинаковых элементов хранить не может. При печати слова могут меняются случайным образом
print(courses)
# на входе могут быть дубликаты, но на выходе их нет
courses = {'History', 'Math', 'Programming', 'Literature', 'Physics', 'Math'}
print(courses)
print(len(courses))
# можно удалить элементы и даже дублированные не будут показываться
courses.remove('Math')
print(courses)
print(len(courses))

deleted = courses.pop()
print(deleted)
# в первую очередь set (множество) нужен для того, чтобы избавиться от дубликатов, но изменяется порядок


set1 = {'History', 'Math', 'Programming', 'Literature', 'Physics'}
set2 = {'Physics', 'Art', 'Dising', 'Literature', 'History'}

print(set1.intersection(set2))
# данный метод нужен для определения - что общего между двумя сетами (множествами).
# Со списками и кортежем данный метод не применим.
# Можно менять местами
print(set2.intersection(set1))
# паказать различие можно методом difference
print(set1.difference(set2))
print(set2.difference(set1))
# можно объединить два set  в один set
print(set1.union(set2))

numbers1 = [5, 6, 3, 8, 12, 33, 31, 13]
print(set(numbers1))
# при первом чтении цифр порядок, как бы сохраняется, но индексов ВСЁ-РАВНО нет
