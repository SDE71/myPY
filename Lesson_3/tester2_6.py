courses = ['History', 'Math', 'Programming', 'Literature', 'Physics']
numbers = [1, 13, 6, 0.232, -123, 4, 7, 9, 11]

empty_list = []
empty_list1 = list()
empty_tuple = ()
empty_tuple1 = tuple()
empty_set = {}
empty_set1 = set()
print(type(empty_list))
print(type(empty_list1))
print(type(empty_tuple))
print(type(empty_tuple1))
print(type(empty_set))
# пустой set (множество) можно объявить только set(). Иначе будет выходить словарь
print(type(empty_set1))
print('Разделение печати')
# если хочу объявить список из одного элемента, то есть нюансы
empty_list = [1]
empty_tuple = (1)
empty_set = {1}
print(type(empty_list))
print(type(empty_tuple))
print(type(empty_set))
print('Разделение печати')
# если в списке и множестве это могу сделать, то в кортеже скобки имеют приоритет математики (),
# для объявления одного элемента в кортеже нужно делать с запятой
empty_list = [1]
empty_tuple = (1,)
empty_set = {1}
print(type(empty_list))
print(type(empty_tuple))
print(type(empty_set))
