import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
df = pd.read_excel(r'C:\Users\吴雨馨\Downloads\IBMS1 practical 2.4 Measuring homeostatic changes data(3)(1).xlsx', sheet_name='Sheet1')
sns.barplot(x="Stressor",y="HR changes (bpm)",data=df,width=0.5,palette="Purples")
plt.title("Students' HR changes during different stressors")
plt.show()