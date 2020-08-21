#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

"""
Created on Mon Feb 10 13:47:55 2020

@author: gleb
"""

friends = [70,  65,  72,  63,  71,  64,  60,  64,  67]            #друзья
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]           #минуты
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' ]           #метки

plt.scatter(friends, minutes)

#назначить метку для каждой точки
for label, friend_count, minute_count in zip(labels,friends,minutes):
    plt.annotate(label,
                 xy = (friend_count, minute_count),   #задать метку
                 xytext = (5, -5),                    #и немного ее сместить
                 textcoords = 'offset points')

plt.title("Зависимость между колличеством минут и числом друзей")
plt.xlabel("Число друзей")
plt.ylabel("Время, проводимое на сайте ежедневно, мин")
plt.grid(True, linestyle = ':', alpha = 0.4, axis = 'both')
plt.show()