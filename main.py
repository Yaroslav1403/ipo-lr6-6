import random

#Создание случайного списка из 20 значений по 4 случайных целых чисел от -10 до 10
random_values = [[random.randint(-10, 10) for _ in range(4)] for _ in range(20)]

#Находим универсальные комбинации пар из этих значений
universal_pairs = set()
#Внешний цикл проходится по всем элементам списка
for a in range(len(random_values)):
    #Внутренний цикл перебирает элементы, которые идут после текущего элемента внешнего цикла
    for b in range(a + 1, len(random_values)):
        #Каждая пара подсписков добавляется в множество как кортеж для обеспечения уникальности
        universal_pairs.add((tuple(random_values[a]), tuple(random_values[b])))

#Вывод всех универсальных пар, которые были собраны в universal_pairs
print("Универсальные комбинации пар:")
for pair in universal_pairs:
    print(pair)

#Просим пользователя ввести целое число
input_user = int(input("Введите целое число: "))

#Инициализируется счетчик count, который будет считать количество пар, сумма которых меньше введенного пользователем числа
count = 0

#Cуммируются элементы первого (pair[0]) и второго (pair[1]) подсписков
for pair in universal_pairs:
    pair_sum = sum(pair[0]) + sum(pair[1])
    #Если полученная сумма меньше введенного числа, счетчик увеличивается на 1.
    if pair_sum < input_user:
        count += 1

#Вывод результата
print("Количество пар, чья сумма меньше", input_user, ":", count)