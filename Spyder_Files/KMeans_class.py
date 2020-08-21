#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 21:03:28 2020

@author: gleb
"""


from functools import partial
import math, random



def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result


def scalar_multiply(c, v):
    return [c*v_i for v_i in v]


def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


def vector_substract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


def squared_distance(v, w):
    """(v_1 - w_1)**2 + ... +(v_n - w_n)**2"""
    return sum_of_squares(vector_substract(v, w))


class KMeans:
    """Выполняет кластеризацию по методу к средних"""
    
    def __init__(self, k):
        self.k = k          # число кластеров 
        self.means = None   #средние кластеров 
        
        
    def classify(self, input):
        """вернуть индекс кластера близжайшего к значению input"""
        return min(range(0, self.k), key=lambda i: squared_distance(input, self.means[i]))
    
    
    def train(self, inputs):
        #выбрать к случайных точек в качестве средних
        self.means = random.sample(inputs, self.k)
        assigenments = None
        while True:
            #найти новые значения
            new_assigenments = list(map(self.classify, inputs))
            
            #если ни одно значение не изменилось то завершить
            if assigenments == new_assigenments:
                print("...training_finished...")
                return
            
            #в противном случае сохранить новые значения
            assigenments = new_assigenments
            if assigenments:
                print(len(assigenments), ": len of assigenments")
            
            #и вычислить новые средние на их основе
            for i in range(self.k):
                #найти все точки назначенные кластеру i
                i_points = [p for p, a in zip(inputs, assigenments) if a == i]
                
                #проверить что i_points не пуст чтоб не делить на 0
                if i_points:
                    self.means[i] = vector_mean(i_points)
            
 



           
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


path_to_png_file = r"/Users/gleb/pic_Random/kolobok_yobaVers.png"

img = mpimg.imread(path_to_png_file)




pixels = [pixel for row in img for pixel in row]



def recolor_image(k=5):

    img = mpimg.imread(path_to_png_file)
    pixels = [pixel for row in img for pixel in row]
    clusterer = KMeans(k)
    clusterer.train(pixels) # this might take a while

    def recolor(pixel):
        cluster = clusterer.classify(pixel) # index of the closest cluster
        return clusterer.means[cluster]     # mean of the closest cluster

    new_img = [[recolor(pixel) for pixel in row]
               for row in img]

    plt.imshow(new_img)
    plt.axis('off')
    plt.show()
          

recolor_image()           
            
            
            
            
            
            
            
            
            
            
            