#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

"""
Created on Wed Feb 12 00:59:40 2020

@author: gleb
"""

#Скалярное призведение (векторов)
def dot(v, w):
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))

#Рассчет суммы квадратов
def sum_of_squares(v):
    return dot(v, v)


#Вернет среднее для переданного списка
def mean(x:[int]):
    return sum(x) / len(x)


#Вернет вектор отклонений от среднего
def de_mean(x):
    """Пересчитать вектор х, вычтя его среднее из каждого элемента
        (среднее результата будет = 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


#Дисперсия это средняя сумма квадратов отклонения от среднего 
#В англ. носит имя variance
def variance(x):
    """Предполагается что вектор х состоит минимум из 2-ух элементов"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n-1)


#Стандартное отклонение - корень из дисперсии (variance)
def standart_deviation(x):
    return math.sqrt(variance(x))


#Ковариантность
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n-1)
    

#Корреаляция
def correlation(x,y):
    stdev_x = standart_deviation(x)
    stdev_y = standart_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x /stdev_y
    else:
        return 0    #Если переменные не меняются то корреляция равна 0


x = [-2, -1, 0, 1, 2]
y = [99.98, 99.99, 100, 100.05, 100.05]

print(correlation(x, y))















    