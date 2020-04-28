import numpy
import matplotlib.pyplot as plt
import argparse
import os

'''
author = Song Jian
'''

parser = argparse.ArgumentParser()
parser.add_argument('-input', default = '', help = 'input file')
parser.add_argument('-label', default = '', help = 'label file')
parser.add_argument('-output', default = '', help = 'output file')
parser.add_argument('-select', default = '', help='choose class')
parser.add_argument('-py',default = '', help='choose py')

args = parser.parse_args()
dirs = os.listdir(args.input)
name_list=[name for name in dirs if name[len(name)-4:] == '.txt']
init_name = [filename for filename in dirs if filename[len(filename)-4:] == '.txt']

if args.select == 'plot':
	name_l = []
	for i in name_list:
		name_l.append(i.strip('_results.txt'))
	select = 'python special_plot.py'
	for i,name in enumerate(name_l):
		print(select + ' -input ' +args.input + init_name[i] +' -output ' + args.output + '/' + name + '_plot' + ' -highlight ' + args.label + ';')


else:
	select = 'sudo python LargeVis_run.py '
	for i,name in enumerate(name_list):
		print(select + ' -input ' +args.input + init_name[i] +' -output ' + args.output + '/' + name + '_results.txt' + ';')






	





