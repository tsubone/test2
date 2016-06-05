#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

import math as m

#plt.style.use('ggplot')

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



# 2D Graph draw

x = np.arange (0.01, 1, 0.01)

# r is low string to avoid escape sequence
plt.title (r"$-[a\log (x) + (1-a)\log (1-x)]$");
plt.xlabel(r'$x$')
plt.ylabel (r'$y$');

a = 0.1
y =  - (a * np.log (x) + (1-a) * np.log (1-x))
plt.plot (x, y, label="a=0.1")

a = 0.4
y =  - (a * np.log (x) + (1-a) * np.log (1-x))
plt.plot (x, y, label="a=0.4")

a = 0.8
y =  - (a * np.log (x) + (1-a) * np.log (1-x))
plt.plot (x, y, label="a=0.8")

plt.xlim (0.0,1.0)
plt.xticks (np.arange(0,1.1,0.1))
plt.legend(loc='upper top') # 凡例を右上に表示
plt.show();


# 3D Graph draw

x = np.arange(0.01, 1, 0.01)
y = np.arange(0.01, 1, 0.01)
X, Y = np.meshgrid(x, y)
Z = -(Y * np.log (X) + (1-Y) * np.log(1-X))

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.plot_wireframe(X,Y,Z) #<---ここでplot

plt.show()

print (dir ())

