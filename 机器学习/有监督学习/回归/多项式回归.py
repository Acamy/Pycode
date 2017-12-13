import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
 
datasets_X = []
datasets_Y = []
fr = open('prices.txt','r',encoding= 'utf-8')
lines = fr.readlines()
for line in lines:
    items = line.strip().split(',')
    datasets_X.append(float(items[0]))
    datasets_Y.append(int(items[1]))
 
length = len(datasets_X)
datasets_X = np.array(datasets_X).reshape([length,1])
datasets_Y = np.array(datasets_Y)
 
minX = min(datasets_X)
maxX = max(datasets_X)
X = np.arange(minX,maxX).reshape([-1,1])

# 线性回归
linear = linear_model.LinearRegression()
linear.fit(datasets_X, datasets_Y)

# 多项式回归
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(datasets_X)
lin_reg_2 = linear_model.LinearRegression()
lin_reg_2.fit(X_poly, datasets_Y)

# 绘图
plt.figure(figsize=(12,7)) #设置图片大小
plt.scatter(datasets_X, datasets_Y, color = 'green',marker='.')
plt.plot(X, linear.predict(X), color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()