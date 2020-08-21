#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from collections import Counter

"""
Created on Mon Feb 10 12:20:55 2020

@author: gleb
"""

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade//10 * 10     #вернет число полных 10-ов
histogram = Counter(decile(grade) for grade in grades)

#Видимо в новой версии центрирование столбцов происходит автоматически 
#и потому нет нужды смещать х (на 4 влево в данном случае)
#но вот как было раньше:
#plt.bar([x - 4 for x in histogram.keys()],
#        histogram.values(),
#        8)

plt.bar([x for x in histogram.keys()],     #сдвинуть столбец влево на 4
         histogram.values(),                 #высота столбца 
         8)                                  #ширина каждого столбца 8

plt.axis([-5, 105, 0, 5])                    #ось Х от -5 до 105
                                             #ось У от 0 до 5
                                             
plt.xticks([10 * i for i in range(11)])      #метки по оси Х: 0,10,...,100
plt.xlabel("Дециль")
plt.ylabel("Число студентов")
plt.title("Распределение оценок за экзамен №1")
plt.grid(True, alpha = 0.5, linestyle = ':')  #настройка сетки разметки (по умолчанию нет)
plt.show()


