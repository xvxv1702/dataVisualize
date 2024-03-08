# 导入我们所需的库 as：即给库取别名，方便书写
import matplotlib.pyplot as plt
import numpy as np

path = r"D:\learn\research\optimization\result\RunTimeDataset\result.csv"
pop_count = 6 #种群数量
pop_size = 20#子种群大小
max_generation = 1500
# title =
# 绘图
# 1. 确定画布
plt.figure(figsize=(10, 5))  # figsize:确定画布大小

data = np.loadtxt(open(path,"rb"),
                  delimiter=",",#分隔符
                  skiprows=1,#跳过前n行
                  usecols=range(4,4+pop_size))#读取的列的范围


generation = int(len(data)/pop_count)
id_count = len(data[0])


colors = ['blue','yellow','magenta','cyan','black', 'tomato','yellowgreen']
x = []
y = []
for m in range(pop_count):

    for i in range(generation):
        if i > max_generation:
            break
        raw = i * pop_count + m
        for j in range(id_count):
            y.append(data[raw][j])
            x.append(i)
plt.scatter(x,  # 横坐标
            y,  # 纵坐标
            c='gray',  # 点的颜色
            label='Individual',# 标签 即为点代表的意思
            s = 0.05)  #点的大小

#绘制平均fitness
data = np.loadtxt(open(path,"rb"),
                  delimiter=",",#分隔符
                  skiprows=1,#跳过前n行
                  usecols=range(4,4+pop_size))#读取的列的范围

x2 = []
y2 = []

for i in range(generation):
    if i >= max_generation :
        break
    sum = 0.0
    for j in range(id_count):
        sum += data[i][j]
    equalFitness = sum / id_count;
    y2.append(equalFitness)
    x2.append(i)

plt.plot(x2, #横轴值
         y2,#纵轴值
         'r*-', #'bo-'表示蓝色实线，数据点实心原点标注,'s'方块,'o'实心圆点，'*'五角星
         alpha=0.5,#透明度
         linewidth=1,#线的宽度
         label='EqualFitness',#标签
         markersize = 1
         )

#绘制最大fitness
data = np.loadtxt(open(path,"rb"),
                  delimiter=",",#分隔符
                  skiprows=1,#跳过前n行
                  usecols=[3])#读取的列的范围

generation = int(len(data)/pop_count)

styles = ['bo-','yo-','mo-','co-','ko-','go-','ro-']
for m in range(pop_count):
    x1 = []
    y1 = []
    for i in range(generation):
        if i > max_generation:
            break
        raw = raw = i * pop_count + m
        y1.append(data[raw])
        x1.append(i)

    label = 'group'+str(m)
    style = styles[m]
    plt.plot(x1, #横轴值
             y1,#纵轴值
             style, #'bo-'表示蓝色实线，数据点实心原点标注,'s'方块,'o'实心圆点，'*'五角星
             alpha=0.5,#透明度
             linewidth=1,#线的宽度
             label=label,#标签
             markersize = 1
             )

x2 = []
y2 = []
for i in range(generation):
    if i > max_generation:
        continue
    tempMax = 0
    for m in range(pop_count):
        raw = raw = i * pop_count + m
        if(tempMax < data[raw]):
            tempMax = data[raw]
    y2.append(tempMax)
    x2.append(i)

plt.plot(x2, #横轴值
             y2,#纵轴值
             'go-', #'bo-'表示蓝色实线，数据点实心原点标注,'s'方块,'o'实心圆点，'*'五角星
             alpha=0.8,#透明度
             linewidth=4,#线的宽度
             label='BestFitness',#标签
             markersize = 1
             )


# 3.展示图形
plt.legend()  # 显示图例
plt.grid(True)#显示网格背景
#坐标轴范围
# plt.ylim((3,6))
#plt.xlim((0,max_generation))
#坐标轴名字000000
plt.xlabel("Generation",fontsize = 12)
plt.ylabel("Fitness",fontsize = 12)
#标题
# plt.title(title)
plt.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.9, wspace=0.1, hspace=0.1)
plt.legend(loc='upper left')

plt.show()  # 显示所绘图形
#plt.savefig(r'D:\learn\research\dataVisualize\test.jpg')  # 图片名可自定义(必须写图片名称.jpg),与plt.show不可同时使用

