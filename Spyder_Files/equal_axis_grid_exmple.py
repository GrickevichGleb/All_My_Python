#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

"""
Created on Mon Feb 10 14:04:45 2020

@author: gleb
"""

test_1_grades = [99, 90, 85, 97, 80]  #оценки за тест 1
test_2_grades = [100, 85, 60, 90, 70] #оценки за тест 2

plt.scatter(test_1_grades, test_2_grades)
plt.title("Несопоставимые оси")  
plt.xlabel("Оценки за тест 1")
plt.ylabel("оценки за тест 2")
plt.grid(alpha = 0.4) 
plt.show()

#для того чтобы получить сопоставимые оси
#необходимо вызвать метод plt.axis("equal")

plt.scatter(test_1_grades, test_2_grades)
plt.axis("equal")
plt.title("Cопоставимые оси")  
plt.xlabel("Оценки за тест 1")
plt.ylabel("оценки за тест 2")
plt.grid(alpha = 0.4) 
plt.show()