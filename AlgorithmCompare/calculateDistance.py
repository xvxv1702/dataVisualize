# 计算精英集的平均距离

# 导入我们所需的库 as：即给库取别名，方便书写
import matplotlib.pyplot as plt
import numpy as np
import os
from natsort import ns, natsorted  # 排序库

root = r"D:\learn\research\optimization\result\20240421AlgorithmCompare\distanceCompare"
pop_size = 24  # ssiea的


def calculate_distance(list1, list2):
    length = pop_size
    sum_distance = 0
    for m in range(length):
        sum_distance += (list1[m] - list2[m]) * (list1[m] - list2[m])
    return sum_distance ** 0.5


def main():
    src_listdir = os.listdir(root)
    src_listdir = natsorted(src_listdir, alg=ns.PATH)

    for file in src_listdir:
        file_path = os.path.join(root, file)
        data = np.loadtxt(open(file_path, "rb"),
                          delimiter=",",  # 分隔符
                          skiprows=1,  # 跳过前n行
                          usecols=range(1, pop_size + 1))  # 读取的列的范围

        length = len(data)
        sum_distance = 0
        count = 0
        for i in range(length-1):
            for j in range(i+1,length):
                sum_distance += calculate_distance(data[i],data[j])
                count +=1

        equal_distance = sum_distance/count

        print(file + "结果："+str(equal_distance))


main()
