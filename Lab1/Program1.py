# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 22:18:50 2023

@author: mognc
"""

import numpy as np
import matplotlib.pyplot as plt

values = np.random.randint(10, size=(100))
plt.plot(values)

plt.title('Random Noise using Test Program')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
