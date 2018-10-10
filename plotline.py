#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:04:09 2018

@author: rodrigos
"""

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
y = np.full((1000,),25)
ax.plot(y,x);
