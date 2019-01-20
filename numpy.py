# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 09:01:01 2019

@author: 903
"""

import numpy as np

my_matrix = np.loadtxt(open("data-detail.txt", "rb"), delimiter=",", skiprows=0)
Data = my_matrix[:, 1:101]
print(Data)
