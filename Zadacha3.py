x = int(input('Введите значение точки X: '))
y = int(input('Введите значение точки Y: '))

if x > 0 and y > 0:
    print(f'X = {x}; Y = {y} | 1 четверть')
elif x < 0 and y > 0:
    print(f'X = {x}; Y = {y} | 2 четверть')
elif x < 0 and y < 0:
    print(f'X = {x}; Y = {y} | 3 четверть')
elif x > 0 and y < 0:
    print(f'X = {x}; Y = {y} | 4 четверть')
else:
    print('ОШИБКА!')