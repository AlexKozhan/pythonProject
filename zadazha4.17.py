# import math
# triangle, circle = int(input('Площадь треугольника равна ')), float(input('Площадь круга равна '))
# h = int(input('Высота треугольника равна '))
# a = 2*triangle/h
# r = math.sqrt (circle / math.pi)
# if r <=math.sqrt(3) * a / 6:
#     print('Круг влезет')
# else:
#     print('Не влезет')

import math
triangle, circle = int(input('Площадь треугольника равна ')), float(input('Площадь круга равна '))
h = int(input('Высота треугольника равна '))
a = 2*triangle/h
r = math.sqrt (circle / math.pi)
if r <=math.sqrt(3) * a / 3:
    print('Треугольник влезет')
else:
    print('Не влезет')