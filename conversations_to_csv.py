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

    
def selectFileToSave(name):
    if re.match('Zuzanna', name):
        file = 'input_text.txt'
    else:
        file = 'output_text.txt'
    return file


def input_and_output(line_number):
    input_txt = open('input_text.txt', encoding="utf-8")
    all_inputs = input_txt.readlines()
    #print(f"{all_inputs[line_number]}")
    output_txt = open('output_text.txt', encoding="utf-8")
    all_outputs = output_txt.readlines()
    #print(f"{all_outputs[line_number]}")
    return all_inputs[line_number], all_outputs[line_number]

#with open('input_text.txt', 'a') as input_text, open('output_text.txt', 'a') as output_text:
    
for file_number in range (19, 0, -1):
    contents = open(f"MyFriend_YJX3MkSiqQ/message_{file_number}.html", encoding="utf-8").read()
    soup = BeautifulSoup(contents, 'lxml')
    lists = soup.select(".pam._3-95._2pi0._2lej.uiBoxWhite.noborder")
    temp_name = lists[0].select("._3-96._2pio._2lek._2lel")[0].getText()
    file = selectFileToSave(temp_name)
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
                        with open(file, 'a', encoding = "utf-8", newline='') as f:
                            if name != temp_name:
                                f.write('\n')
                                file = selectFileToSave(name)
                                temp_name = name
                            print(string)
                            f.write(string.strip("\n") + ' ')
                            

                            
num_entry_lines = sum(1 for line in open('input_text.txt', encoding="utf-8"))
print(num_entry_lines)
num_output_lines = sum(1 for line in open('output_text.txt', encoding="utf-8"))
print(num_output_lines)



import pandas as pd
df_input = pd.read_csv('input_text.txt',  sep="\t", names = ['input'])
df_target = pd.read_csv('output_text.txt',  sep="\t", names = ['target'])
df = pd.concat([df_input, df_target], axis=1, sort=False)
df.to_csv('conversations.csv')
