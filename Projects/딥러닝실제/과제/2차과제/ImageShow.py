# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 20:36:47 2021

@author: KSS
"""

import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('ImageTest.jpg')

plt.imshow(img)
plt.show()
