#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

a = np.arange(16).reshape((2,8))
b = np.arange(16,32,1).reshape((2,8))
c = np.vstack((a,b))

print a, a.shape
print b, b.shape
print c, c.shape

