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
import re
    

for file_number in range (1, 0, -1):
    contents = open(f"MyFriend_YJX3MkSiqQ/message_{file_number}.html", encoding="utf-8").read()
    soup = BeautifulSoup(contents, 'lxml')
    lists = soup.select(".pam._3-95._2pi0._2lej.uiBoxWhite.noborder")
    temp_name = lists[0].select("._3-96._2pio._2lek._2lel")[0].getText()
    print(temp_name)
    for lis in reversed(lists): 
        name = lis.select("._3-96._2pio._2lek._2lel")[0].getText() 
        entries = lis.find_all("div", {"class": "_3-96 _2let"}) 
        for entry in entries: 
            texts = entry.find_all("div")
            for item in texts: 
                string = item.find("div", text=True)#.getText()
                if string != None:
                    string = string.getText()
                    if not re.match("http.*", string): 
                        if name != temp_name:
                            print(name)
                            temp_name = name
                        print(string)