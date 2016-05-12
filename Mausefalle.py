# -*- coding: utf-8 -*-
"""
Mauseffalle or Folow that mouse
Written by EBG
The MIT License (MIT)
Copyright (c) 2016 Evan B. Goldstein

die rolls
1 nothing
2 red
3 hole you came in
4 red 
5 red
6 green

0 is start

trap-> 2 turns
28

holes:
4 r0, g6
11 r7 g14
17 r13 g19
20 r17 g23
26 r24 g27
32 r28 g34
34 finish

@author: ebgoldstein
"""

import matplotlib.pyplot as plt
import numpy as np

x=0
counter=0

while x<=34:

    if x==4:
        roll=np.random.randint(1,6)
        if roll==2 or roll==4 or roll==5:
            x=0
        if roll==6:
            x=6
    elif x==11:
        roll=np.random.randint(1,6)
        if roll==2 or roll==4 or roll==5:
            x=7
        if roll==6:
            x=14
    elif x==17:
        roll=np.random.randint(1,6)
        if roll==2 or roll==4 or roll==5:
            x=13
        if roll==6:
            x=19
    elif x==20:
        roll=np.random.randint(1,6)
        if roll==2 or roll==4 or roll==5:
            x=17
        if roll==6:
            x=23
    elif x==26:
        roll=np.random.randint(1,6)
        if roll==2 or roll==4 or roll==5:
            x=24
        if roll==6:
            x=27
    elif x==28:
        counter=counter+2
        roll=np.random.randint(1,6)
        x=x+roll
    elif x==32:
        roll=np.random.randint(1,6)
        if roll==2 or roll==4 or roll==5:
            x=28
        if roll==6:
            x=34
    else:
        roll=np.random.randint(1,6)
        x=x+roll
    
    counter=counter+1

print(counter)
