#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from http://qiita.com/sz_dr/items/c8435e4b740e40db8bec

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import math

#与えられた標本から最尤推定を用いて平均と分散を求める関数
def predict(data):
    mu = np.mean(data)
    var = np.var(data, ddof=1)  #不偏推定量を用いる
    return mu, var

def main():
    #平均mu, 標準偏差stdのガウス分布に従う標本をN個生成する
    mu = 3.0
    v = 2.0
    std = math.sqrt(v)
    N = 10000
    data = np.random.normal(mu, std, N)
    #最尤推定を行い, 平均と分散を求める
    mu_predicted, var_predicted = predict(data)
    #分散の値から標準偏差を求める
    std_predicted = math.sqrt(var_predicted)
    print("original: mu={0}, var={1}".format(mu, v))
    print(" predict: mu={0}, var={1}".format(mu_predicted, var_predicted))
    
    #結果のプロット
    plt.hist(data, bins=40, normed=True, alpha=0.5)

    xs = np.linspace(min(data), max(data), 200)
    norm = mlab.normpdf(xs, mu_predicted, std_predicted)
    plt.plot(xs, norm, color="red")
    plt.xlim(min(xs), max(xs))
    plt.xlabel("x")
    plt.ylabel("Probability")
    plt.show()

    
if __name__ == '__main__':
    main()

