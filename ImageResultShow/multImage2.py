# 使用matplotlib展示多张图片
import cv2
import matplotlib
import matplotlib.pyplot as plt
import os
from natsort import ns, natsorted  # 排序库
import numpy as np

path = r"D:\learn\research\optimization\result\20240321sixGroup0.4update0.3mute\final"
sheet_path = path + r"\bestIndividualList.csv"
plane_folder = os.path.join(path, "plane")
perspective_folder = os.path.join(path, "perspect")


# 6类，6行，每行14列
categries = 6
collums = 19
count_each_pop = 20


def collect_image_path(plane_folder_path: str, perspective_folder_path: str):
    # assert os.path.exists(root), "dataset root: {} does not exist.".format(root)
    plane_image = []
    perspective_image = []

    cla_path = plane_folder_path  # 子文件夹的路径
    listdir = os.listdir(cla_path)
    listdir = natsorted(listdir, alg=ns.PATH)  # 要加alg=ns.PATH参数才和windows系统名称排序一致
    for i in listdir:
        ful_path = os.path.join(cla_path, i)
        perspective_image.append(ful_path)

    cla_path = perspective_folder_path  # 子文件夹的路径
    listdir = os.listdir(cla_path)
    listdir = natsorted(listdir, alg=ns.PATH)  # 要加alg=ns.PATH参数才和windows系统名称排序一致
    for i in listdir:
        ful_path = os.path.join(cla_path, i)
        plane_image.append(ful_path)

    return plane_image, perspective_image


plane_image_path, perspective_image_path = collect_image_path(plane_folder, perspective_folder)
print(plane_image_path)

fig = plt.figure()

# 读取表格
fitness_list = np.loadtxt(open(sheet_path, "rb"),
                          delimiter=",",  # 分隔符
                          skiprows=1,  # 跳过前n行
                          usecols=3)  # 读取的列的范围

# 绘制表头
# colorList = ['#4C4A59', '#1B7F7A', '#0897B4', '#F2CDAC', '#4CABA6']
colorList = ['#4C4A59', '#1D8058', '#0897B4', '#F5BA8D', '#714d69', '#a6915c']
groups = ['LShape', 'UShape', 'Base', 'Other','ParShape','WithYard']
for i in range(categries):
    plt.subplot(categries, collums, i * collums + 1)
    group = groups[i]
    plt.text(0,0.5,group, fontsize=10, horizontalalignment='center', verticalalignment='center',
              color=colorList[i], weight='bold')
    # plt.title( group, fontsize=10, horizontalalignment='center', verticalalignment='center',
    #          color=colorList[i], weight='bold')
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')

# 绘制图片
image_collum = collums - 1
for i in range(categries):
    color = colorList[i]
    for j in range(1, collums):
        # 读取图片
        image_id = i * count_each_pop + j - 1
        plane_img = cv2.imread(plane_image_path[image_id])
        perspective_img = cv2.imread(perspective_image_path[image_id])
        img_vstack = np.vstack((plane_img, perspective_img))
        # print(str(image_id))

        matplotlib.rc('axes', edgecolor=color)

        # 绘制轴测
        ax2 = fig.add_subplot(categries, collums, i * collums + j+1)
        plt.imshow(img_vstack)
        fitness = round(fitness_list[image_id], 4)
        plt.title(fitness, fontsize=8, color=colorList[i])
        plt.xticks([])
        plt.yticks([])

# 调整格式
plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95,wspace=0.1,hspace=0.3)
# plt.title(title)
# 展示图片
plt.show()
