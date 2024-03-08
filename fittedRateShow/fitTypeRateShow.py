# 读取totalDetailResult.csv文件，并计算每个种群中typeid和subpopution契合的比例，并可视化
import os
import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

root = r"./totalDetailResult.csv"
pop_count = 6  # 种群数量
pop_size = 20  # 子种群大小
gene_length = 30  # gene长度
max_generation = 50

# 读取表格,格式：generation,subPopulation,id,fitness,gene,
data = np.loadtxt(open(root, "rb"),
                  delimiter=",",  # 分隔符
                  skiprows=1,  # 跳过前n行
                  usecols=[1, 2])  # 读取的列的范围
data = data[:max_generation * pop_count * pop_size, :]

generation = int(len(data) / pop_count / pop_size)

styles = ['b-', 'y-', 'm-', 'c-', 'k-', 'g-', 'r-']
pop_names = ["LShape", "Ushape", "basic", "other", "parShape", "withYard"]

# pop = 1
for pop in range(pop_count):
    x = []
    y = []
    style = styles[pop]
    label = pop_names[pop]
    for i in range(generation):
        # if i % 2 != 0:
        #     y.append(y[-1])
        #     x.append(i)
        #     continue
        if i > max_generation:
            continue
        fit_tag = 0
        for j in range(pop_size):
            raw = i * pop_count * pop_size + pop * pop_size + j
            if data[raw][0] == data[raw][1]: fit_tag += 1
        y.append(fit_tag / float(pop_size))
        x.append(i)
    m = make_interp_spline(x, y, 3)
    xs = np.linspace(0, 40, 500)
    ys = m(xs)
    plt.plot(xs,  # 横轴值
             ys,  # 纵轴值
             style,  # 'bo-'表示蓝色实线，数据点实心原点标注,'s'方块,'o'实心圆点，'*'五角星
             alpha=1,  # 透明度
             linewidth=1,  # 线的宽度
             label=label,  # 标签
             markersize=1
             )
plt.legend()  # 显示图例
plt.xlabel("Generation",fontsize = 12)
plt.ylabel("Rate",fontsize = 12)
plt.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.9, wspace=0.1, hspace=0.1)
plt.show()  # 显示所绘图形
