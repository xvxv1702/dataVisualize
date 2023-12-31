# 使用matplotlib展示多张图片
import cv2
import matplotlib
import matplotlib.pyplot as plt
import os
from natsort import ns, natsorted   # 排序库
import numpy as np

def collect_image_path(root: str):
    assert os.path.exists(root), "dataset root: {} does not exist.".format(root)

    image_path = []

    listdir = os.listdir(root)
    listdir = natsorted(listdir, alg=ns.PATH)  # 要加alg=ns.PATH参数才和windows系统名称排序一致
    for i in listdir:
        ful_path = os.path.join(root,i)
        image_path.append(ful_path)

    return image_path

image_folder_path = r"D:\learn\research\optimization\result\20231231grouptransferVisualize\1parent"
csv_path = r"D:\learn\research\optimization\result\20231231grouptransferVisualize\1parent.csv"
group_size = 16
collums = 9
group_count = 4
rows = 8

#读取图片
image_path = collect_image_path(image_folder_path)
#读取表格
data = np.loadtxt(open(csv_path,"rb"),
                  delimiter=",",#分隔符
                  skiprows=1,#跳过前n行
                  usecols=[1])#读取的列的范围
sub_group_count = [0,0,0,0]
for i in data:
    id = int(i)
    sub_group_count[id] += 1



# colorList = ['#4C4A59', '#1B7F7A', '#0897B4', '#F2CDAC', '#4CABA6']
colorList = ['#4C4A59', '#1D8058', '#0897B4', '#F5BA8D', '#4CABA6']
groups = ['LShape', 'UShape', 'Base', 'Other']

fig = plt.figure(figsize=(10, 8))

print(image_path)
print(len(image_path))
print(sub_group_count)
#绘制表头
for i in range(group_count):
    title = 'group' + str(i)
    # plt.subplot(rows, collums, (i*2) * collums + 1)
    # plt.text(0.5, 0.5, title, fontsize=15, horizontalalignment='center', verticalalignment='center',
    #          color=colorList[i])
    # plt.xticks([])
    # plt.yticks([])
    # plt.axis('off')

    plt.subplot(rows, collums, (i * 2+1) * collums + 1)
    plt.title(title, fontsize=15, horizontalalignment='center', verticalalignment='center',
              color=colorList[i])
    group = '(' + groups[i] + ')'
    plt.text(0.5, 0.5, group, fontsize=10, horizontalalignment='center', verticalalignment='center',
             color=colorList[i])
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')


#绘制图片
tempId = 0
for i in range(group_count):
    color = colorList[i]
    for j in range(group_size):
        print(tempId)
        if(j < sub_group_count[i]):
            # 读取图片
            image = cv2.imread(image_path[tempId])
            tempId += 1
            # 绘制平面
            matplotlib.rc('axes', edgecolor=color,linewidth=3)
            loc = i*2*collums + j + 2
            if (j>collums-2):loc+=1
            ax1 = fig.add_subplot(rows, collums, loc)
            plt.imshow(image)
            plt.xticks([])
            plt.yticks([])
            # plt.subplots_adjust(hspace=0.2)
        # else:
        #     loc = i * 2 * collums + j + 2
        #     if (j > collums - 2): loc += 1
        #     ax1 = fig.add_subplot(rows, collums, loc)
        #     plt.xticks([])
        #     plt.yticks([])

#调节间距
plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0.1, hspace=0.2)
plt.show()
