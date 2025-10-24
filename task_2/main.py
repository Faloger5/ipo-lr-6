#Доброва Анна
import random #иморт модуля 
values = [-15, -4, -2, -7, 0, 3, 5, 12, 9]#список возможных значений
rows = random.randint(4, 8)#выбор кол-ва строк
cols = random.randint(4, 8)#выбор кол-ва элементов в строке
matrix = []#пустая матрица 
for _ in range(rows):#цикл для каждой строки
    row = [random.choice(values) for i in range(cols)]#заполняем строки цифрами
    matrix.append(row)#добавляем каждое значение в конец
print("Матрица " + str(rows) + "x" + str(cols) + ":")#выводит формат матрицы
for row in matrix:#цикл для перебора строк
    print(" ".join("{:>4}".format(num) for num in row))#выводит матрицу 
sum = 0#счетчик суммы 
for row in matrix:#перебор каждой строки
    for num in row:#перебор каждого элемента
        if num % 3 != 0:#если число некратно 3
            sum += num#вычисление суммы
print("\nСумма элементов, некратных 3:", sum)#вывод результата суммы
