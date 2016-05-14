#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import matplotlib.pyplot as plt
# import numpy as np
# from sklearn.datasets import fetch_mldata
# from chainer import cuda, Variable, FunctionSet, optimizers
# import chainer.functions  as F
# import sys

import numpy as np

import chainer
from chainer import computational_graph
from chainer import cuda
import chainer.links as L
from chainer import optimizers
from chainer import serializers

import data
import net

import matplotlib.pyplot as plt

plt.style.use('ggplot')



def draw_digit(data,n):
    size = 28
    plt.subplot(10,10,n)
#    X, Y = np.meshgrid(range(size),range(size))
    Z = data.reshape(size,size)   # convert from vector to 28x28 matrix
    Z = Z[::-1,:]             # flip vertical
    plt.xlim(0,27)
    plt.ylim(0,27)
#    plt.pcolor(X, Y, Z)
    plt.pcolor(Z)
    plt.gray()
    plt.tick_params(labelbottom="off")
    plt.tick_params(labelleft="off")

plt.figure(figsize=(28, 28))

n_units = 1000
# Prepare multi-layer perceptron model, defined in net.py
model = L.Classifier(net.MnistMLP(784, n_units, 10))

# Setup optimizer
optimizer = optimizers.Adam()
optimizer.setup(model)

initmodel='mlp.model'
resume='mlp.state'

# Init/Resume
print('Load model from', initmodel)
serializers.load_npz(initmodel, model)
print('Load optimizer state from', resume)
serializers.load_npz(resume, optimizer)

print ("===============\n")
print (model.predictor.l1.W.data);
print ("----------------\n")
print (model.predictor.l1.W);

cnt=1
for idx in range(100):
    draw_digit(model.predictor.l1.W.data[idx],cnt)
    cnt+=1;

plt.show()
