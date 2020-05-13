#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :Numpy01.py
@Time         :2020/05/06 22:53:48
@Version      :1.0
@Notes        :
'''
import numpy as np 

#数组属性
array=np.array([[1,2,3],[2,3,4]]) #数组
print(array.ndim)  #维数
print(array.shape) #行列数
print(array.size)  #一共多少个元素
print()
#数组创建
a=np.array([2,23,4],dtype=np.int)            #创建整型数组
b=np.array([[2,23,4],[1,3,5]],dtype=np.int)  #创建二维数组
c=np.zeros((3,4))    #创建一个3行4列的0值数组
d=np.ones((3,4))     #创建一个3行4列的全部为1的数组
e=np.empty((3,4))    #创建一个3行4列的空值数组
f=np.arange(10,20,2)  #生成10到20步长为2的数列
g=np.arange(12).reshape((3,4))  #生成为3行4列的矩阵数列
h=np.linspace(1,10,20)   #生成20段的数列，即20个值
i=np.linspace(1,10,6).reshape((2,3))   #生成20段的数列矩阵
print()
#基础运算-数组计算
t3a=np.array([10,20,30,40])
t3b=np.arange(4)
t3c=t3a-t3b
t3d=t3c**2  #平方
print(t3d<4)  #返回对每个值的判断结果
print()
#基础运算-矩阵运算
t4a=np.array([[1,1],[0,1]])
t4b=np.arange(4).reshape((2,2))
print(t4a)
print(t4b)
t4c=t4a*t4b  #逐个相乘
print(t4c)
t4d=np.dot(t4a,t4b) #矩阵乘法
t4d2=t4a.dot(t4b)  #是上一行矩阵乘法的另一种写法
print(t4d)
t4e=np.random.random((2,4)) #随机创建2*4的矩阵
print(np.max(t4e)) #矩阵中的最值
print(np.min(t4e)) #矩阵中的最值
print(np.sum(t4e)) #矩阵中的最值
print(np.max(t4e,axis=1)) #矩阵中每一列的最值
print(np.max(t4e,axis=0)) #矩阵中每一行的最值