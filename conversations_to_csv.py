# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 10:45:26 2020

@author: zuzan
"""

from bs4 import BeautifulSoup 
import requests 
import pandas as pd
from pandas.compat import StringIO
import matplotlib.pyplot as plt
import numpy as np
import itertools
import networkx as nx
import collections
#import igraph
    
    
#contents = open("MyFriend_YJX3MkSiqQ/message_1.html", encoding="utf-8").read()
#soup = BeautifulSoup(contents, 'lxml')
#lists = soup.find_all("div", {"class": "pam _3-95 _2pi0 _2lej uiBoxWhite noborder"})
#for lis in lists: 
#    names = lis.find_all("div", {"_3-96 _2pio _2lek _2lel"}) 
#    print(names)
#    entries = lis.find_all("div", {"class": "_3-96 _2let"}) 
#    for entry in entries: 
#        texts = entry.find_all("div")
#        for item in texts: 
#            string = item.find_all("div") 
#            print(string)

contents = open("MyFriend_YJX3MkSiqQ/message_2.html", encoding="utf-8").read()
soup = BeautifulSoup(contents, 'lxml')
lists = soup.select(".pam._3-95._2pi0._2lej.uiBoxWhite.noborder")
for lis in lists: 
    name = lis.select("._3-96._2pio._2lek._2lel")[0].getText() 
    print(name)
    entries = lis.find_all("div", {"class": "_3-96 _2let"}) 
    for entry in entries: 
        texts = entry.find_all("div")
        for item in texts: 
            string = item.find("div", text=True)#.getText()
            if string != None:
                string = string.getText()
                
            print(string)