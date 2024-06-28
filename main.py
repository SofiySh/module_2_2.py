# Задача "Все ли равны?"
print('Введите три числа для сравнения.')
first = int(input('Первое число: '))
second = int(input('Второе число: '))
third = int(input('Третье число: '))
print('Колличество одинаковых чисел:')
if first == second == third:
    print('3')
elif first == third and second != third or third == second and second != first or first == second and second != third:
    print('2')
else:
    print('0')

    # девятую строку можно сократить до elif first == second or second == third or first == third: