# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 10:51:14 2021

@author: Elton
"""









#%%

with open("E:/Python/Project/test.txt") as f:
    lines = f.readlines()

lines # ['This is the first line.\n', 'This is the second line.\n']

new=[]
for line in lines:
    new.append(line[6:])
    
with open("E:/Python/Project/createshow.py","w") as f:
    f.writelines(new)

#%%
with open("E:/Python/Project/Pages/register.py") as f:
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
        
    

with open("E:/Python/Project/Pages/register.py","w") as f:
    f.writelines(new)

#%%
with open("E:/Python/Project/Moviebase/Pages/home.py") as f:
    lines = f.readlines()

lines # ['This is the first line.\n', 'This is the second line.\n']

import re

pattern=re.compile("support")
pattern2=re.compile("Toplevel1")
pattern3=re.compile("^\t")
pattern4=re.compile("^\t\t")

new=[]
for line in lines:
    temp=""
    while True:
        if pattern3.search(line):
            line=line[1:]
            temp+="    "
        else:
            break
    new.append(temp+line)
        
    

with open("E:/Python/Project/Moviebase/Pages/home.py","w") as f:
    f.writelines(new)



