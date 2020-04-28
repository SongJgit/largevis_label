#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import argparse
'''
author = Song Jian
'''

# 参数块设置
parser = argparse.ArgumentParser()
parser.add_argument('-input', default = '', help = 'input file')
parser.add_argument('-output', default = '', help = 'output file')
parser.add_argument('-range', default = '', help = 'axis range')
parser.add_argument('-highlight',default ='',help='high light label')
args = parser.parse_args()

# 获取需要高亮显示的向量及其标签
# 字典的key为向量index，value为标签
if args.highlight != '':
    shs_data = {}
    for i in open(args.highlight):
        high_vec = i.strip().split(' ')
        shs_data[int(high_vec[1])] = int(high_vec[0])
#print(shs_data)

# 获取经过largevis降维的向量
# i是largevis结果的行索引（0起始），因为结果第一行是向量数量信息，因此i-1之后相当于向量由0起始的4，可以与label的index相对应。
#查看第i-1个向量是否存在于shs_data中，如果存在，则该向量为需要打标签的向量。
# all_data的key为需要高亮的向量号，不需要高亮的key为-1，value为向量坐标以及标签，字典的长度为shs_data+1
N = M = 0
all_data = {}
for i, line in enumerate(open(args.input)):
    vec = line.strip().split()
    if i == 0:
        N = int(vec[0])
        M = int(vec[1])
    elif i <= N and args.highlight != '':
        if i-1 in sorted(shs_data.keys()):
            vec.append(shs_data[i - 1])
            all_data.setdefault(int(i-1), []).append((float(vec[-3]), float(vec[-2]), int(vec[-1])))
        else:
            vec.append(int(-1))
            all_data.setdefault(int(-1), []).append((float(vec[-3]), float(vec[-2]), int(vec[-1])))
#print(all_data)

# 画图,x为x坐标列表，y为y坐标列表，z为标签列表,ll为标签
colors = plt.cm.rainbow(np.linspace(0,1,len(all_data)))
for color, ll in zip(colors, sorted(all_data.keys())):
    #print(ll)
    x = [t[0] for t in all_data[ll]]
    y = [t[1] for t in all_data[ll]]
    z = [t[2] for t in all_data[ll]]
    if ll == -1:
        plt.scatter(x, y,s=10,color=color)
    else:
	lab = z[0]
        plt.scatter(x, y, color=color, label= z[0], s=10 )
	#添加点的标注，有缺陷，不需要就将其注释掉
	plt.annotate(lab,xy = (x[0], y[0]))
	#添加角标
	plt.legend()
plt.savefig(args.output, dpi = 500)


