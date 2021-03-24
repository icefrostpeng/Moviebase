# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 10:51:14 2021

@author: Elton
"""


with open("sidebar.py") as f:
    lines = f.readlines()

lines # ['This is the first line.\n', 'This is the second line.\n']

import re

pattern=re.compile("support")
pattern2=re.compile("Toplevel1")
pattern3=re.compile("^    ")
pattern4=re.compile("^        ")

new=[]
for line in lines:
    
    if pattern.search(line):
        continue
    temp=line[6:]
    if pattern4.search(line):
        line="\t\t"+line[8:]
    if pattern3.search(line):
        line="\t"+line[4:]
        
    new.append(line)
        
    

with open("sidebar.py","w") as f:
    f.writelines(new)






