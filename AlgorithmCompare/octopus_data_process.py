# 将octopus的txt结果存为csv

import matplotlib.pyplot as plt
import numpy as np
import os
import csv
from natsort import ns, natsorted  # 排序库

src_root = (
    r"D:\learn\research\optimization\rhinoModel\AlgorithmCompare\OctopusExport_20240311test_preEnv _octopus.gh_2024426__14_7_14")
param_root = (
    r"D:\learn\research\optimization\rhinoModel\AlgorithmCompare\OctopusExport_20240311test_preEnv _octopus.gh_2024426__14_7_0")
dest_path = r"D:\learn\research\optimization\result\20240421AlgorithmCompare\octopus\octopus_2024426__14_7_14.csv"

header = ['generation', 'bestFitness', 'fitness', 'gene']
with open(dest_path, 'w', encoding='utf8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

x = []
y = []
plt.figure(figsize=(8, 5))  # figsize:确定画布大小

src_listdir = os.listdir(src_root)
src_listdir = natsorted(src_listdir, alg=ns.PATH)
param_listdir = os.listdir(param_root)
param_listdir = natsorted(param_listdir, alg=ns.PATH)
# src_listdir = src_listdir.sort()
# print(src_listdir)

data_list = []
generation = 0
best_fitness = 0
out_data_list = []
for text_file in src_listdir:
    file_path = os.path.join(src_root, text_file)
    param_file = text_file.replace('objectives', 'parameters')
    param_path = os.path.join(param_root, param_file)
    # 读取参数文件
    with open(param_path, 'r') as file:
        param_list = []  # 存储整个文件的参数
        line_param = []  # 存储一组参数
        # 逐行读取并打印内容
        for line in file:
            if line.strip():
                data_string = line.strip()  # 去除行尾的换行符
                try:
                    param = float(data_string)
                    line_param.append(param)
                    # print(param)
                except ValueError:
                    # 如果无法转换为浮点数，则忽略该单词
                    pass
            else:
                if line_param:
                    # print(line_param)
                    param_list.append(line_param)
                    line_param = []

    # 打开文件
    with open(file_path, 'r') as file:
        out_data = []
        individual_count = 0
        # 逐行读取并打印内容
        for line in file:
            if line.strip():
                data_string = line.strip()  # 去除行尾的换行符
                try:
                    fitness = float(data_string) * (-1)
                    data_list.append(fitness)
                    if best_fitness < fitness:
                        best_fitness = fitness
                    out_data = [str(generation), str(best_fitness), str(fitness)]
                    out_data = out_data + param_list[individual_count]
                    # print(out_data)
                    out_data_list.append(out_data)
                    # print(fitness)  # 打印浮点数
                    individual_count +=1
                except ValueError:
                    # 如果无法转换为浮点数，则忽略该单词
                    pass
        x.append(generation)
        y.append(best_fitness)
        generation += 1
with open(dest_path, 'a+', encoding='utf8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(out_data_list)
    # for data in out_data_list:
    #     writer.writerow(data)

plt.plot(x,  # 横轴值
         y,  # 纵轴值
         'r*-',  # 'bo-'表示蓝色实线，数据点实心原点标注,'s'方块,'o'实心圆点，'*'五角星
         alpha=0.8,  # 透明度
         linewidth=1,  # 线的宽度
         label='Fitness',  # 标签
         markersize=1
         )
plt.show()
