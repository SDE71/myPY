# user_input = float(input('Please inter something: '))
# user_input = float(user_input)

# print(user_input)
# print(user_input)
# print(user_input)
#
# print(type(user_input))

a = float(input('Side A: '))
b = float(input('Side B: '))
c = float(input('Side C: '))

half_p = (a + b + c) / 2

area = (half_p * (half_p - a) * (half_p - b) * (half_p - c)) ** 0.5
print(area)
print(type(area))


# print(half_p)
