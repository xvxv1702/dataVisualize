# 导入我们所需的库 as：即给库取别名，方便书写
import matplotlib.pyplot as plt
import numpy as np

path = r"D:\learn\research\optimization\result\RunTimeDataset\result.csv"
data = np.loadtxt(open(path,"rb"),
                  delimiter=",",#分隔符
                  skiprows=1,#跳过前n行
                  usecols=range(4,64))#读取的列的范围

generation = len(data)
id_count = len(data[0])

x = []
y = []

for i in range(generation):
    for j in range(id_count):
        y.append(data[i][j])
        x.append(i)

#绘制平均fitness
x2 = []
y2 = []

for i in range(generation):
    sum = 0.0
    for j in range(id_count):
        sum += data[i][j]
    equalFitness = sum / id_count;
    y2.append(equalFitness)
    x2.append(i)

#绘制最大fitness
data = np.loadtxt(open(path,"rb"),
                  delimiter=",",#分隔符
                  skiprows=1,#跳过前n行
                  usecols=[3])#读取的列的范围

generation = len(data)
x1 = []
y1 = []
for i in range(generation):
    y1.append(data[i])
    x1.append(i)

#绘制每代当前最大fitness
data = np.loadtxt(open(path,"rb"),
                  delimiter=",",#分隔符
                  skiprows=1,#跳过前n行
                  usecols=[2])#读取的列的范围

generation = len(data)
x3 = []
y3 = []
for i in range(generation):
    y3.append(data[i])
    x3.append(i)


# 定义数据
# x = np.random.rand(10)  # 取出10个随机数
# y = x + x ** 2 - 10  # 用自定义关系确定y的值

# 绘图
# 1. 确定画布
plt.figure(figsize=(8, 4))  # figsize:确定画布大小

# 2. 绘图
plt.scatter(x,  # 横坐标
            y,  # 纵坐标
            c='red',  # 点的颜色
            label='fitness',# 标签 即为点代表的意思
            s = 0.2)  #点的大小


plt.plot(x1, #横轴值
         y1,#纵轴值
         'bs--', #'bo-'表示蓝色实线，数据点实心原点标注,'s'方块,'o'实心圆点，'*'五角星
         alpha=0.5,#透明度
         linewidth=1,#线的宽度
         label='BestFitness',#标签
         markersize = 1
         )

plt.plot(x2, #横轴值
         y2,#纵轴值
         'g*-', #'bo-'表示蓝色实线，数据点实心原点标注,'s'方块,'o'实心圆点，'*'五角星
         alpha=0.8,#透明度
         linewidth=1,#线的宽度
         label='EqualFitness',#标签
         markersize = 1
         )

plt.plot(x3, #横轴值
         y3,#纵轴值
         'yo-', #'bo-'表示蓝色实线，数据点实心原点标注,'s'方块,'o'实心圆点，'*'五角星
         alpha=0.5,#透明度
         linewidth=1,#线的宽度
         label='CurrentBestFitness',#标签
         markersize = 1
         )

# 3.展示图形
plt.legend()  # 显示图例
plt.grid(True)#显示网格背景

plt.show()  # 显示所绘图形
#plt.savefig(r'D:\learn\research\dataVisualize\test.jpg')  # 图片名可自定义(必须写图片名称.jpg),与plt.show不可同时使用

