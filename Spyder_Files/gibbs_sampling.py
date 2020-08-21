#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 17:51:55 2020

@author: gleb
"""

import random
from collections import defaultdict


#бросить кубик
def roll_a_die():
    return random.choice([1,2,3,4,5,6])


# Х ЭТО ЗНАЧЕНИЕ КУБИКА 1, А У ЭТО СУММА ДВУХ КУБИКОВ


#прямая выборка
def direct_sample():
    d1 = roll_a_die()
    d2 = roll_a_die()
    return d1, d1+d2


#случайное у в зависимости от х
def random_y_given_x(x):
    """ равновероятное значение будет х+1, х+2, ..., х+6 """
    return x + roll_a_die()


#случайное х в зависимости от у
def random_x_given_y(y):
    if y <= 7:
        #если сумма <= 7, первый кубик равновероятно будет равен
        #1, 2, ..., (сумма - 1)
        return random.randrange(1, y)
    else:
        #если сумма > 7 то первый кубик равновероятно будет
        #(сумма - 6), (сумма - 5), ..., 6
        return random.randrange(y-6, 7)
    

#Выборка по Гиббсу
def gibbs_sample(num_iters = 100):
    x, y = 1,2  #не важно какие на самом деле
    
    for _ in range(num_iters):
        x = random_x_given_y(y)   #случайное х в зависимости от у
        y = random_y_given_x(x)   #случайное у в зависимости от х
    return x, y


#сравнить распределения 
def compare_distributions(num_samples = 1000):
    counts = defaultdict(lambda: [0, 0])
    for _ in range(num_samples):
        counts[gibbs_sample()][0] += 1
        counts[direct_sample()][1] += 1
    return counts

result = compare_distributions()
print(result)






        
    