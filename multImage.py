# 使用matplotlib展示多张图片
import cv2
import matplotlib
import matplotlib.pyplot as plt
import os
from natsort import ns, natsorted   # 排序库
import numpy as np

def collect_image_path(root: str):
    assert os.path.exists(root), "dataset root: {} does not exist.".format(root)

    # 遍历文件夹，一个文件夹对应一个类别,返回文件夹列表
    picture_folders = [cla for cla in os.listdir(root) if os.path.isdir(os.path.join(root, cla))]
    # 排序，保证顺序一致
    picture_folders.sort()

    plane_image_path = []
    perspective_image_path = []

    cla = picture_folders[0]
    cla_path = os.path.join(root, cla)  # 子文件夹的路径
    listdir = os.listdir(cla_path)
    listdir = natsorted(listdir, alg=ns.PATH)  # 要加alg=ns.PATH参数才和windows系统名称排序一致
    for i in listdir:
        ful_path = os.path.join(root, cla, i)
        perspective_image_path.append(ful_path)

    cla = picture_folders[1]
    cla_path = os.path.join(root, cla)  # 子文件夹的路径
    listdir = os.listdir(cla_path)
    listdir = natsorted(listdir, alg=ns.PATH)  # 要加alg=ns.PATH参数才和windows系统名称排序一致
    for i in listdir:
        ful_path = os.path.join(root, cla, i)
        plane_image_path.append(ful_path)



    return plane_image_path, perspective_image_path


path =r"D:\learn\research\optimization\result\20231208ImageResultShow"

plane_image_path, perspective_image_path = collect_image_path(path)
print(plane_image_path)

fig = plt.figure()


#4类，8行，每行15列
categries = 4
collums = 18
count_each_pop = 25

#读取表格
sheet_path = path + r"\currentGeneration.csv"
fitness_list = np.loadtxt(open(sheet_path,"rb"),
                  delimiter=",",#分隔符
                  skiprows=1,#跳过前n行
                  usecols=3)#读取的列的范围

#绘制表头
colorList = ['#4C4A59', '#1B7F7A', '#0897B4', '#F2CDAC', '#4CABA6']
groups = ['LShape', 'UShape', 'Base', 'Other']
for i in range(categries):
    plt.subplot(categries * 2, collums, (i * 2) * collums + 2)
    plt.text(0.5, 0.5, 'Plane', fontsize=10, horizontalalignment='center', verticalalignment='center',
             color=colorList[i])
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')

    plt.subplot(categries * 2, collums, (i * 2+1) * collums + 2)
    plt.title("Fitness", fontsize=10, horizontalalignment='center', verticalalignment='center',
              color=colorList[i])
    plt.text(0.5, 0.5, 'Perspect', fontsize=10, horizontalalignment='center', verticalalignment='center',
             color=colorList[i])
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')

    plt.subplot(categries * 2, collums, (i * 2+1) * collums + 1)
    group = groups[i]
    plt.title(group, fontsize=10, horizontalalignment='center', verticalalignment='center',
              color=colorList[i], weight='bold')
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')

image_collum = collums - 2
for i in range(categries):
    color = colorList[i]
    for j in range(2,collums):
        #读取图片
        plane_img = cv2.imread(plane_image_path[i*count_each_pop + j])
        perspective_img = cv2.imread(perspective_image_path[i * count_each_pop + j])
        print(str(i*count_each_pop + j))

        matplotlib.rc('axes', edgecolor=color)
        #绘制平面
        ax1 = fig.add_subplot(categries*2, collums, (i*2)*collums + j+1)
        plt.imshow(plane_img)
        plt.xticks([])
        plt.yticks([])
        plt.subplots_adjust(hspace=0.4)
        # ax = plt.gca()  # 获取当前的axes

        #绘制轴测
        ax2 = fig.add_subplot(categries * 2, collums, (i*2+1) * collums + j+1)
        plt.imshow(perspective_img)
        fitness = round(fitness_list[i*count_each_pop + j],4)
        plt.title(fitness, fontsize=8, color=colorList[i])
        plt.xticks([])
        plt.yticks([])


plt.show()
