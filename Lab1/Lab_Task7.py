# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:16:10 2023

@author: mognc
"""

import numpy as np
import matplotlib.pyplot as plt

cgpa = np.random.randint(4, size=(8))
plt.plot(cgpa)

plt.title('Cgpa over the semesters')
plt.xlabel('Semester')
plt.ylabel('CGPA')
plt.show()