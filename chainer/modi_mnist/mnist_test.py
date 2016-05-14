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
import chainer.functions  as F
from chainer import optimizers
from chainer import serializers

import data
import net

import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Prepare dataset
print('load MNIST dataset')
mnist = data.load_mnist_data()
mnist['data'] = mnist['data'].astype(np.float32)
mnist['data'] /= 255
mnist['target'] = mnist['target'].astype(np.int32)

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

print("test_data_b=", mnist['data'][0])
print("test_data_b2=", mnist['data'])
hoge=np.array([1.0,3.0]);
print ("hoge=", hoge);

#test_data=chainer.Variable(mnist['data'][0])
#test_data=chainer.Variable(np.array([mnist['data'][0], mnist['data'][1]]))
test_data=chainer.Variable(np.array([mnist['data'][7]]))
#test_data=chainer.Variable(mnist['data'])
print("test_data=", test_data)

#print ("func=", F.relu())

output=model.predictor(test_data)
print("output=", F.softmax(output).data, mnist['target'][7])


