#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

a = np.arange(4*4*4).reshape((4,4,4))

b = np.where(a%2==0)

print b
