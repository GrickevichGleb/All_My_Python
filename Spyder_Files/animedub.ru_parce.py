#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 17:05:52 2020

@author: gleb
"""

from bs4 import BeautifulSoup
import requests


def find_titles(url, soup):
    url = url
    soup = soup
    
    anime_titles_full = []
    anime_titles_rus = []
    
    divs = soup('div', 'mov clearfix')
    print("***** divs found *****")
    for div in divs:
        title2 = div.find('div','mov-i img-box')
        anime_titles_full.append(title2.find('img').get('alt'))
    
    for title in anime_titles_full:
        anime_titles_rus.append(title.split("/")[0])
        
    res_tuple = anime_titles_full, anime_titles_rus
    return res_tuple


def multi_page(n):
    
    names = []

    base_url = "https://animedub.ru/page/"
    for p in range(1, n+1):
        new_url = base_url + str(p) + "/"
        soup = BeautifulSoup(requests.get(new_url).text, 'html.parser')
        
        names.append(find_titles(new_url, soup))
    return names

base = multi_page(3)
for p in range(3):
    print(base[p][1])
    print("**********************")
    
    














