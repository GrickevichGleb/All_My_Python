#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 14:18:46 2020

@author: gleb
"""

#Не смог я это разобрать) 

from bs4 import BeautifulSoup
import requests
 
html = requests.get("https://myanimelist.net").text
soup = BeautifulSoup(html, 'html.parser')

first_paragraph = soup.find_all('p')   #первый тег <р>, можно просто soup.p

first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()

all_paragraphs = soup.find_all('p')
paragraphs_with_class = [p for p in soup('p') if p.get("class")]

title_paragraphs = soup('p', {'class' : 'title'})
#print(title_paragraphs)
title_paragraphs2 = soup('p', 'title')
#print(title_paragraphs2)
title_paragraphs3 = [p for p in soup('p') if 'title' in p.get('class', [])]
#print(title_paragraphs3)

#элементы <span> внутри элементов <div>
#предупреждение: вернет тот же span несколько раз
#если он находится внутри нескольких элементов <div>
#нужно учитывать 
#<div> это секция (контейнер) а <span> это  generic inline
#container for inline elemnts and content
#it used to group elements for styling purposes (by using the class or id atributes)
span_inside_divs = [span                        #для каждого <div>
                    for div in soup('div')      #на странице 
                                                #найти каждый <span>
                    for span in div('span')]    #внутри него

print(span_inside_divs)