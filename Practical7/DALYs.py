import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir(r"C:\Users\吴雨馨\Downloads")
#os.getcwd()
#os.listdir()
dalys_data = pd.read_csv("dalys-rate-from-all-causes(1).csv")
print(dalys_data.head(5))
print(dalys_data.info())
print(dalys_data.describe())
my_columns = [True, True, False, True]
dalys_data.iloc[0:3,my_columns]

#fetch all the lines of Afghanistan
afghanistan_data = dalys_data[dalys_data["Entity"] == "Afghanistan"]
print(afghanistan_data)

#fetch lines of China
china_data=dalys_data[dalys_data["Entity"]=="China"]
china_data=china_data.iloc[0: ,[0,2,3]]
DALYs_mean = np.mean(china_data['DALYs'])
DALYs_2019 = china_data.iloc[-1]['DALYs']

#check whether the DALYs of 2019 in China outweights the mean
if DALYs_mean < DALYs_2019:
    print("The DALYs of 2019 outweight the mean value.")
else:
    print("The DALYs of 2019 doesn't outweight the mean.")

#draw the scatter plot
plt.plot(china_data.Year, china_data.DALYs, 'b+')
plt.xticks(china_data.Year,rotation=-90)
plt.show()

#answer the new question
data_of_2019=dalys_data[dalys_data["Year"] == 2019]
data_of_2019=data_of_2019.iloc[: ,[0,3]]
print(data_of_2019)
plt.plot(data_of_2019.Entity,data_of_2019.DALYs,'r+')
plt.xticks(data_of_2019.Entity,rotation=-90,fontsize=4)
plt.show()

