'''
Дегтярев Виталий (группа 22/08)
Домашнее задание №2.05
Домашняя работа по уроку "Функции в Python.Функция с параметром"
'''
# Задание функции
def get_matrix(n:int, m:int, value:int):
    matrix = [] # Задание списка для матрицы 
    for i in range(n):
        matrix.append([]) # Формирование пустых строк матрицы
        for j in range(m):
            matrix[i].append(value) # Формирование столбцов матрицы со значениями value
    return matrix

# Ввод исходных данных и вызов функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод результатов в консоль
print(f'{result1}')
print(f'{result2}')
print(f'{result3}')