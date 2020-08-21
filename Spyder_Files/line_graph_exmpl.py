#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

"""
Created on Mon Feb 10 13:13:18 2020

@author: gleb
"""

variance = [1, 2 ,4, 8, 16, 32, 64, 128, 256]       #дисперсия
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]   #квадрат смещения

#сумарная ошибка
total_error = [x + y for x,y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

#метод plt.plot можно вызвать много раз,
#чтобы показать несколько графиков на одной диаграме 
#зеленая сплошная линия
plt.plot(xs, variance, 'g-', label = "Дисперсия")
#красная штрих-пунктирная
plt.plot(xs, bias_squared, 'r-.', label = "Смещение^2")
#синяя пунктирная 
plt.plot(xs, total_error, 'b:', label = "Сумарная ошибка")

#Если для каждой линии задано название label
#то легенда будет показана автоматически,
#loc = 9 означает наверху посередине 

plt.legend(loc = 9)
plt.xlabel("Сложность модели")
plt.title("Компромис между смещением и дисперсией")
plt.grid(True, linestyle='-', alpha = 0.4)
plt.show()