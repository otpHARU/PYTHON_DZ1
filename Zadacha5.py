# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x1, y1 = int(input('Введите значение x1: ')), int(input('Введите значение y1: '))
x2, y2 = int(input('Введите значение x2: ')), int(input('Введите значение y2: '))
distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

print(f'A ({x1}, {y1}); B ({x2}, {y2}) —> {round(distance, 3)}')


























