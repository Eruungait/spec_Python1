# Задача №2
# Найти каждую цифру трехзначного числа.
number = str(input('Введите трехзначное число: '))
left = int(number[0])
middle = int(number[1])
right = int(number[2])
print('Первая цифра:', left,
    '\nВторая цифра:', middle,
    '\nТретья цифра:', right)


#через math
import math
number = int(input('Введите трехзначное число: '))
left = int(number / 100)
middle = int((number - left * 100) // 10)
right = int(number % 10)

print('Первая цифра:', left,
    '\nВторая цифра:', middle,
    '\nТретья цифра:', right)
