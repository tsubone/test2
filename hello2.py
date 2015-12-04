#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

print "start hello2"

y = np.array([[2, 3, 4], [4, 5, 6]])
x = np.array([range(10), range(10)])
print y
print x

hoho=[[1,2],[3,4]]
print "hoho=", hoho, hoho[0][0]

m1 = np.matrix([[2,3],[4,5]]);
m2 = np.matrix([[6,7],[8,9]]);

print "m1=", m1
print "m2=", m2
print "m1_11", m1[0,1]


print m1*m2

m3 = np.linalg.inv(m1)

print m3, m1*m3



x=np.arange(-3,3,0.1)
y=np.sin(x)
plt.plot
