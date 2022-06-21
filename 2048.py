#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 21:37:47 2022

@author: jie
"""
import sys
def merge(l):
    m = []
    while 0 in l:
        l.remove(0)
    
    i = 0
    while i < len(l):
        if i < len(l) - 1 and l[i]==l[i+1]:
            m.append(2*l[i])
            i+=2
        else:
            m.append(l[i])
            i+=1         
    while len(m) < 4:
        m.append(0)
    return m         

def g_2048(t):
    direction = t[4]
    tt = [[0]*4 for i in range(4)]
    if direction == 0:
        for i in range(4):
            m = merge([t[i][0],t[i][1],t[i][2],t[i][3]])
            tt[i]=m
    elif direction == 1:
        for j in range(4):
            m = merge([t[0][j],t[1][j],t[2][j],t[3][j]])
            tt[0][j]=m[0]
            tt[1][j]=m[1]
            tt[2][j]=m[2]
            tt[3][j]=m[3]
    elif direction == 3:
        for j in range(4):
            m = merge([t[3][j],t[2][j],t[1][j],t[0][j]])
            tt[3][j]=m[0]
            tt[2][j]=m[1]
            tt[1][j]=m[2]
            tt[0][j]=m[3]                
    elif direction == 2:
        for i in range(4):
            m = merge([t[i][3],t[i][2],t[i][1],t[i][0]])
            tt[i][3]=m[0]
            tt[i][2]=m[1]
            tt[i][1]=m[2]
            tt[i][0]=m[3]
    return tt  

t=[]
i = 0
while i < 4:
    t.append(list(map(int, sys.stdin.readline().strip().split())))
    i += 1   
direction = int(sys.stdin.readline().strip())
t.append(direction)
tt = g_2048(t)
for line in tt:
    line = list(map(str, line))
    print(" ".join(line))
