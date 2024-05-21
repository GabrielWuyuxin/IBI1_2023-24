import matplotlib.pyplot as plt
import numpy as np
timespent={'sleeping':8,'Classes':6,'Studying':3.5,'TV':2,'Music':1}
other=24-timespent['sleeping']-timespent['Classes']-timespent['Studying']-timespent['TV']-timespent['Music']  #caculate the other time apart from time in dict
timespent['other']=other #add the other time into dict.
labels=list(timespent.keys()) #use activities as labels
sizes=list(timespent.values()) #use times as values
average=np.mean(sizes)
print(average)

plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%') #draw the pie graph. I want to show the percentages of timespan of each activity
plt.title('averge time spent in a day') 
plt.show()

