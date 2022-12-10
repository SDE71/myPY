# поработаем ещё раз со списками
courses = ['History', 'Math', 'Programming', 'Literature', 'Phisics']
numbers = [1, 6, 4, 7, 9, 11]

test_list = [1, 2, 3, 4, 5]
print(test_list)
print(test_list[1])

# вызвав элемент из списка через индекс можно изменить элемент с первичным значением на другое значиние
# в кортеже TUPLE (второе значение по англ, - запись) мы не сможем менять значения
test_list[1] = 777
print(test_list[1])
print(test_list)
test_list[1] = 'SEVEN'
print(test_list)
# если сделаем срез из списка и заменим, например, словом SEVEN,
# то идёт разбивка слова по буквам на вызываемое количество элементов из среза
# при этом если вызываешь срез из списка и хочешь заменить значения вызываемых элементов на цифровые
# то будет ошибка
test_list[1:4] = 'SEVEN'
print(test_list)
# но если это будут цифры списком, то получится замена
test_list1 = [1, 2, 3, 4, 5]
test_list1[1:4] = [5, 5, 5, 5]
print(test_list1)
test_list1[1:4] = [5, 5, 5]
print(test_list1)
test_list1[1:4] = [5, 5]
print(test_list1)
test_list1[1:4] = [5]
print(test_list1)
test_list1[1] = ['String']
print(test_list1)
