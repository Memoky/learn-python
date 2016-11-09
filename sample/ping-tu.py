# -*- coding:utf-8 -*-
#import matplotlib.pyplot as plt

import pylab as pl
"""
with open(r"C:\Users\Administrator\Desktop\a1.log") as ins:
    x = []
    for line2 in ins:
        line2=line2.strip('\n')
        x.append(line2)

with open(r"C:\Users\Administrator\Desktop\b1.log") as ins:
    y = []
    for line1 in ins:
        line1 = line1.strip('\n')
        y.append(line1)
"""
def file(url):
    with open(url) as ins:
        y = []
        for line in ins:
            line = line.strip('\n')
            y.append(line)
    return y

x = file(r'C:\Users\Administrator\Desktop\b1.log')
w = file(r'C:\Users\Administrator\Desktop\a1.log')


pl.plot(w[1:91867],x[1:91867])  # 调用pylab的plot函数绘制曲线
pl.show()  # 显示绘制出的图