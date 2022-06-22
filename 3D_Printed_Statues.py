#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 18:16:24 2022

@author: jie
"""

c = int(input())
if c < 3:
    print(c)
else:      
    n=1
    while 2**n < c:
        n+=1
    print(n+1)