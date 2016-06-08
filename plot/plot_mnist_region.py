#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

import csv

#csvfile_path="/home/takashi/work/github/other/chainer_1.6_sda_mnist_sample/hogehoge.csv"
#csvfile_path="/home/takashi/work/github/other/chainer_1.6_sda_mnist_sample/hogehoge2.csv"
csvfile_path="/home/takashi/work/github/other/chainer_1.6_sda_mnist_sample/hogehoge3.csv"

csvfile = open (csvfile_path, "r")

print (csvfile)

ldata=[]
for i in range(10):
    ldata.append([[],[]])

for row in csv.reader(csvfile):
    ldata[int(row[1])][0].append(float(row[2]))
    ldata[int(row[1])][1].append(float(row[3]))

csvfile.close()

my_col=["blue", "blue", "green", "yellow", "cyan", "magenta", "black", "white", "#00ffff", "#00ff00"]

for i in range (10):
    x = np.array(ldata[i][0])
    y = np.array(ldata[i][1])
    plt.scatter (x, y, c=my_col[i], label=str(i))

plt.title("scatter plot of learned mnist feature vector by autoencoder")
plt.xlabel ("x")
plt.xlabel ("y")
plt.legend(loc='upper left')
plt.grid(True)

plt.show()

    



