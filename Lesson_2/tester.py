a = ""
a_1 = "сдрмыдмрымьтмьсмт" \
    "alshsakaks"
a_2 = 'Hello'
a_3 = 'world'

b = ''
c = """"""
c_1 = """
Hello
world
world
"""
d = ''''''
print(a_1)
# при заполнении с одинарными данными в строках gереноса не может быть
print(c_1)
# тройные двойные и одинарные кавычки могут делать перенос строки
print(a_2 + ' ' + a_3)
print(a_2, a_3)
print(a_2 + a_3, 12345)


salary = 1000
user_name = "John"
# new_string = "John's salary is {}"
# фигурные скобки работают вроде как закладки вместо них мы можем что-либо подставить
# print(new_string.format(salary))
# для каждой скруглой скобки должен быть свой аргумент
# new_string = "John's salary is {} {}"
# print(new_string.format(salary, True))
new_string = "{}'s salary is {}"
print(new_string.format(salary, user_name))
new_string = "{1}'s salary is {0}"
print(new_string.format(salary, user_name))
new_string = "{1}'s salary is {0} {1} {0}"
print(new_string.format(salary, user_name))
new_string = "{1}'s salary is {0} {2}"
print(new_string.format(salary, user_name, 'dollars'))

# new_string_1 = 'This {product} cost {price} euros'
# print(new_string_1.format(product = 'computer', price = '1000'))
# можно менять данные местами
# print(new_string_1.format(product = 'computer', price = 1000))

# можно указать после запятой количество знаков через метод f
new_string_1 = 'This {product} cost {price: .2f} euros'
print(new_string_1.format(product='computer', price=1000))

# третий вариант форматированной строки

x = 1234.123123213
y = 123.12312451
print('The value of x %.f' % x)
print('The value of x %.4f' % y)

emp_string = "Hi, my name is %(name)s! I am %(age)f years old" % {'name': 'John', 'age': 30}
print(emp_string)
# - это метод устаревший и он может встречаться в ранних программированиях
# - новый метод ниже
name = 'John'
surname = 'Smith'
age = 30
# print(f'Hi {name + " " + surname}. You are {age - 20} years old')
emp_string = f'Hi {name + " " + surname}. You are {age - 20} years old'
print(emp_string)

bite_sting = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
print(bite_sting.decode('utf-16'))

name_string = 'John Smith'
name_string = name_string.encode('utf-16')
print(name_string)
print(name_string.decode('utf-16'))

# следующее задание использование if, elif и else

x = 8
if x > 10:
    print('X is smoller than 10')
elif x == 5:
    print('X is equal to 5')
elif x == 6:
    print('X is equal to 6')
else:
    print('nothing happened')
print('FINISH')
# elif необязательное условие, но если используется, то else работает на первое if
# если много if используется, то else работает по последнему if

id_code = input('Please enter id: ')
if len(id_code) == 11:
    print('Your id code is ' + id_code)
else:
    if len(id_code) > 11:
        print('Your id code is too long')
    else:
        print('Your id code is too short')
