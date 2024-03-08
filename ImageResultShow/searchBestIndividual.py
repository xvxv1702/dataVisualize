# 用于在完整的记录表格中，找出排名前n的个体，用于后续可视化
import os
import numpy as np
import csv

root = r"D:\learn\research\experiment\result\20240220ushape"
pop_count = 1  # 种群数量
pop_size = 100  # 子种群大小
gene_length = 30  # gene长度
max_generation = 450


# 搜索并写入表格
def search(group: int):
    # 取出子序列
    fitness_list = []
    fitness_index_list = []
    for i in range(data.shape[0]):
        rest = i % 100
        if (group + 1) * pop_size > rest >= group * pop_size:
            fitness_list.append(data[i][3])
            fitness_index_list.append(i)
    # 排序，并获取序号
    sorted_index = np.zeros(pop_size)
    sorted_fitness = np.zeros(pop_size)
    for i in range(len(fitness_list)):
        for j in range(len(sorted_fitness)):
            if fitness_list[i] == sorted_fitness[j]:
                break
            if fitness_list[i] > sorted_fitness[j]:
                sorted_fitness[j] = fitness_list[i]
                sorted_index[j] = i
                break
    # 获取在总列表中的行号
    sorted_index_recover = []
    for i in sorted_index:
        sorted_index_recover.append(fitness_index_list[int(i)])
    # for i in sorted_index_recover:
    #     print(data[i])

    # 写入表格
    with open(output_file_path, 'a+', encoding='utf8', newline='') as f:
        writer = csv.writer(f)
        for i in sorted_index_recover:
            writer.writerow(data[i])


# 读取表格,格式：generation,subPopulation,id,fitness,gene,
input_file_path = os.path.join(root, "totalDetailResult.csv")
data = np.loadtxt(open(input_file_path, "rb"),
                  delimiter=",",  # 分隔符
                  skiprows=1,  # 跳过前n行
                  usecols=range(0, 4 + gene_length))  # 读取的列的范围
data = data[:max_generation * pop_count * pop_size, :]

# 创建表格
name = str(max_generation) + "bestIndividualList.csv"
output_file_path = os.path.join(root, name)
header = ['generation', 'subPopulation', 'id', 'fitness', 'gene']
with open(output_file_path, 'w', encoding='utf8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)

#搜索并写入表格
for id in range(pop_count):
    search(id)
