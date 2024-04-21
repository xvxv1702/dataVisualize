# 用于比较标准遗传算法、ssiea以及本算法的效果

# 导入我们所需的库 as：即给库取别名，方便书写
import matplotlib.pyplot as plt
import numpy as np
import os

root = r"D:\learn\research\optimization\result\20240421AlgorithmCompare"
pop_count = 6
max_generation = 1500

# 获取文件列表
island_folder = os.path.join(root, "island")
standard_folder = os.path.join(root, "standard")
SSIEA_folder = os.path.join(root, "SSIEA")
island_listdir = os.listdir(island_folder)
standard_listdir = os.listdir(standard_folder)
SSIEA_listdir = os.listdir(SSIEA_folder)

# 1. 确定画布
plt.figure(figsize=(10, 5))  # figsize:确定画布大小

# 绘制多岛算法曲线图
temp_id = 0
for file in island_listdir:
    file_path = os.path.join(island_folder, file)
    data = np.loadtxt(open(file_path, "rb"),
                      delimiter=",",  # 分隔符
                      skiprows=1,  # 跳过前n行
                      usecols=[3])  # 读取的列的范围

    generation = int(len(data) / pop_count)

    x2 = []
    y2 = []
    for i in range(generation):
        if i > max_generation:
            continue
        tempMax = 0
        for m in range(pop_count):
            raw = i * pop_count + m
            if tempMax < data[raw]:
                tempMax = data[raw]
        y2.append(tempMax)
        x2.append(i)

    plt.plot(x2,  # 横轴值
             y2,  # 纵轴值
             'go-',  # 'bo-'表示蓝色实线，数据点实心原点标注,'s'方块,'o'实心圆点，'*'五角星
             alpha=0.8,  # 透明度
             linewidth=2,  # 线的宽度
             label='island_algorithm' + str(temp_id + 1),  # 标签
             markersize=1
             )

    temp_id += 1

# 绘制标准遗传算法曲线图
temp_id = 0
for file in standard_listdir:
    file_path = os.path.join(standard_folder, file)
    # 绘制最大fitness
    data = np.loadtxt(open(file_path, "rb"),
                      delimiter=",",  # 分隔符
                      skiprows=1,  # 跳过前n行
                      usecols=[3])  # 读取的列的范围

    generation = len(data)
    x1 = []
    y1 = []
    for i in range(generation):
        if i >= max_generation:
            break
        y1.append(data[i])
        x1.append(i)

    plt.plot(x1,  # 横轴值
             y1,  # 纵轴值
             'bo-',  # 'bo-'表示蓝色实线，数据点实心原点标注,'s'方块,'o'实心圆点，'*'五角星
             alpha=0.5,  # 透明度
             linewidth=2,  # 线的宽度
             label='standard_algorithm' + str(temp_id + 1),  # 标签
             markersize=1
             )

    temp_id += 1

# 绘制SSIEA曲线
generation_size = 20
temp_id = 0
for file in SSIEA_listdir:
    file_path = os.path.join(SSIEA_folder, file)
    # 绘制最大fitness
    data = np.loadtxt(open(file_path, "rb"),
                      delimiter=",",  # 分隔符
                      skiprows=1,  # 跳过前n行
                      usecols=[2])  # 读取的列的范围
    best_fitness = 0.0
    sub_count = 0
    x2 = []
    y2 = []
    generation = 0
    for fitness in data:
        if(generation > max_generation):
            break
        if fitness > best_fitness:
            best_fitness = fitness
        sub_count += 1
        if sub_count == generation_size:
            generation += 1
            x2.append(generation)
            y2.append(best_fitness)
            sub_count = 0

    temp_id += 1
    plt.plot(x2,  # 横轴值
             y2,  # 纵轴值
             'ro-',  # 'bo-'表示蓝色实线，数据点实心原点标注,'s'方块,'o'实心圆点，'*'五角星
             alpha=0.5,  # 透明度
             linewidth=2,  # 线的宽度
             label='SSIEA' + str(temp_id + 1),  # 标签
             markersize=1
             )

# 3.展示图形
plt.legend()  # 显示图例
plt.grid(False)  # 显示网格背景
# 坐标轴范围
# plt.ylim((0,7))
plt.xlim((0, max_generation))
# 坐标轴名字000000
plt.xlabel("Generation", fontsize=12)
plt.ylabel("Fitness", fontsize=12)
# 标题
# plt.title(title)
plt.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.9, wspace=0.1, hspace=0.1)
plt.legend(loc='upper left')

plt.show()  # 显示所绘图形
