#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

import math as m

a = np.arange( 15 ).reshape(3,5)

print a;
print ("============")
#print a[1:,1:5]
#print a[1:,1:5:2]
#print a[1:,:]
print a[:,::-1]
#print a[1:]

b = 1

#print (a, a.shape, a.ndim)
#print (type (a))
#print (type (b))

#x = np.arange (0.01, 1, 0.01)
#print x;

#y =  np.log (x)
#a = 0.4
#y =  - (a * np.log (x) + (1-a) * np.log (1-x))

#print y;

#plt.plot (x, y)
#plt.show();

x = np.arange(0.01, 1, 0.01)
y = np.arange(0.01, 1, 0.01)
X, Y = np.meshgrid(x, y)
Z = -(Y * np.log (X) + (1-Y) * np.log(1-X))

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X,Y,Z) #<---ここでplot

plt.show()

print (dir ())

