"""
На обработку поступает последовательность из 10 целых чисел. Известно, что вводимые числа по
абсолютной величине не превышают 10^6 . Нужно написать программу, которая выводит на экран сумму
всех отрицательных чисел последовательности и максимальное отрицательное число в последовательности.
Если отрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и написал программу неправильно.
Найдите все ошибки в этой программе (их ровно 55). Известно, что каждая ошибка затрагивает только одну строку и может
быть исправлена без изменения других строк.

mx = 0
s = 0
for i in range(11):
    x = int(input())
    if x < 0:
        s = x
    if x > mx:
        mx = x
print(s)
print(mx)
"""
max_num, sum_num = -10 ** 6, 0
for i in range(10):
    num = int(input())
    if num < 0:
        sum_num += num
    if 0 > num > max_num:
        max_num = num

if sum_num < 0:
    print(sum_num, max_num, sep='\n')
else:
    print('NO')
