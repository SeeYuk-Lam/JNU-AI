# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


# 计算梯度和代价
# G = j对w求偏导
def cost_gradient(W, X, Y, n):
    error = X.dot(W) - Y
    ######## Gradient
    # mean默认求平均，把行缩减为1
    G = (error * X).mean(0).reshape(X.shape[1],1)
    #j = ###### cost with respect to current W

    j = (error ** 2).sum() / (2*n)
    return (j, G)

def gradientDescent(W, X, Y, lr, iterations):
    n = np.size(Y)
    # j迭代iterations代
    J = np.zeros([iterations, 1])

    for i in range(iterations):
        # 每一代的j都存在J的列表里面
        (J[i], G) = cost_gradient(W, X, Y, n)
        ####### Update W based on gradient
        W = W - lr * G

    return (W,J)

iterations = 100 ###### Training loops
lr = 1e-5 ###### Learning rate

# 加载数据
# 第一列是x，第二列是y
data = np.loadtxt('LR.txt', delimiter=',')

n = np.size(data[:, 1])
# 2×1的矩阵，第一行是b（w0），第二行是w1
W = np.zeros([2, 1])
# 拼接矩阵，第一列都是1，第二列才是特征x
X = np.c_[np.ones([n, 1]), data[:,0]]
Y = data[:, 1].reshape([n, 1])

(W,J) = gradientDescent(W, X, Y, lr, iterations)

#Draw figure
plt.figure()
plt.plot(data[:,0], data[:,1],'rx')
plt.plot(data[:,0], np.dot(X,W))

plt.figure()
plt.plot(range(iterations), J)
plt.show()