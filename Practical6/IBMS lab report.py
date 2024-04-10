import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
#sns.set(style="darkgrid")
plt.figure()
#figure,(A,B)=plt.subplots(1,2,figsize=(6,6))

##读取数据
#df = pd.read_excel(r'C:\Users\吴雨馨\OneDrive\文档\IBMS1 practical 2.4 Measuring homeostatic changes data(3)(1) 的副本.xlsx', sheet_name='Physical-HR')
#df = pd.read_excel(r'C:\Users\吴雨馨\OneDrive\文档\IBMS1 practical 2.4 Measuring homeostatic changes data(3)(1) 的副本.xlsx', sheet_name='Physical-BP')
#df = pd.read_excel(r'C:\Users\吴雨馨\OneDrive\文档\IBMS1 practical 2.4 Measuring homeostatic changes data(3)(1) 的副本.xlsx', sheet_name='Psychological-HR')
df = pd.read_excel(r'C:\Users\吴雨馨\OneDrive\文档\IBMS1 practical 2.4 Measuring homeostatic changes data(3)(1) 的副本.xlsx', sheet_name='Psychological-BP')
#print(df.head(106))
#plt.boxplot(x, notch=None, sym=None, vert=None, whis=None, positions=None, widths=None, patch_artist=None, meanline=None, showmeans=None, showcaps=None, showbox=None, showfliers=None, boxprops=None, labels=None, flierprops=None, medianprops=None, meanprops=None, capprops=None, whiskerprops=None)


##画箱线图
#sns.boxplot(data=df.loc[:, ['Baseline', '8 min after onset','Offset','Offset + 5 min','Offset + 10 min']],palette="Purples")
#sns.boxplot(data=df.loc[:, ['Baseline', '8 min after onset','Offset','Offset + 5 min','Offset + 10 min']],palette="Purples")
#sns.boxplot(data=df.loc[:, ['Baseline', 'Near onset','Offset','Offset + 5 min','Offset + 10 min']],palette="Purples")
sns.boxplot(data=df.loc[:, ['Baseline', 'Near onset','Offset','Offset + 5 min','Offset + 10 min']],palette="Purples")

## 添加扰动点
# add stripplot
#sns.stripplot(data=df.loc[:, ['Baseline', '8 min after onset','Offset','Offset + 5 min','Offset + 10 min']],color="darkblue", jitter=0.2, size=4)
sns.stripplot(data=df.loc[:, ['Baseline', 'Near onset','Offset','Offset + 5 min','Offset + 10 min']],color="darkblue", jitter=0.2, size=4)

#add title
#plt.title("Students' HR during physical stressor")
#plt.title("Students' BP during physical stressor")
#plt.title("Students' HR during psychological stressor")
plt.title("Students' BP during psychological stressor")

#add x&y label
plt.xlabel('Stages')
#plt.ylabel('HR')##第一第三张
plt.ylabel('BP')##第二张第四张
plt.show()