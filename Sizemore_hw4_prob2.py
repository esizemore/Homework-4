#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 09:55:51 2017

@author: elizabethsizemore
"""

from numpy import exp
from random import random

N=1000000


def randompoints():
    rand_value= (random())**2
    return rand_value



for x in range(N):
    temp=randompoints()
    i=(temp**(-1/2))/(exp(temp)+1)
    
I=(1/N)*i
print (I)

