# largevis
可视化标签，以及命令批量生成 
![results](https://github.com/SJiangit/largevis_label/blob/master/img/netscienceLBW_CFM_q_exp_6presentation_plot.png)
## special_plot
用途：对largevis降维的数据进行标签可视化，为特殊节点加入标签  
环境：Ubuntu、python2.7（自带）  
库：numpy、matplotlib、argparse  
输入文件格式：  
txt 左列为标签，右列为该标签对应的向量，0起始，比如78是第5条向量，应为4.  
使用方法：  
python special_plot.py -input 1461/netscienceLBW_psedu_q_exp_3presentation_results.txt -output netscienceLBW_psedu_q_exp_3presentation_plot -highlight 1461/label/label.txt;  

## command_creat
用途：  
适用于批量生成命令，比如批量生成largevis运行语句，批量生成special_plot语句，避免一次执行一个的麻烦。  
环境：ubuntu、python2.7（自带）  
库：os、argparse  
参数设置：  
-input 输入路径   path/  
-output 输出路径  path/  
-select 可选参数，功能选择 plot则为special_plot,置空则为largevis，默认为空  
-label 可视化时的标签文件，默认为空，功能选择置空时该项无效  
使用方法：  
将需要批量处理的文件放入一个文件夹作为输入文件夹，设定好输出图像的文件夹（special_lot），或者设定好输出降维结果的文件夹（largevis）  
python command_creat.py -input 1461/ -label 1461/label/label.txt -output 1461/img -select plot -py special_plot.py  
example：  
现在在1461文件夹下有18个降维后的结果等待标签可视化，逐个输入命令较为麻烦，使用command_creat  
使用方法：  
将需要批量处理的文件放入一个文件夹作为输入文件夹，设定好输出图像的文件夹（special_lot），或者设定好输出降维结果的文件夹（largevis）  
python command_creat.py -input 1461/ -label 1461/label/label.txt -output 1461/img -select plot -py special_plot.py  
