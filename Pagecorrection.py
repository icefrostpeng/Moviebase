# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 10:51:14 2021

@author: Elton
"""

with open("E:/Python/Project/test.txt") as f:
    lines = f.readlines()

lines # ['This is the first line.\n', 'This is the second line.\n']


new=[]
for line in lines:
    new.append(line[6:])

with open("E:/Python/Project/home.py","w") as f:
    f.writelines(new)


#%%
import re
with open("E:/Python/Project/test.txt") as f:
    lines = f.readlines()

lines # ['This is the first line.\n', 'This is the second line.\n']

pattern=re.compile("place")
new=[]
for line in lines:
    if pattern.search(line):
        new.append(line)
    
with open("E:/Python/Project/out.txt","w") as f:
    f.writelines(new)





