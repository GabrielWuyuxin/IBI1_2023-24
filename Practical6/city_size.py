import matplotlib.pyplot as plt
uk_cities=[0.56,0.62,0.04,9.7]
china_cities=[0.58,8.4,29.9,22.2]
uk_cities.sort()
china_cities.sort()
print(uk_cities)
print(china_cities)
#these are two lists of city sizes of UK and China
china_citynames=['Haining','Hangzhou','Shanghai','Beijing']
uk_citynames=['Edinburgh','Glasgow','Stirling','London']
plt.figure()
#set two subplots to be in the same figure
figure,(fig1,fig2)=plt.subplots(2,1,figsize=(8,6))
#draw the two bar graphs with x-values, height, and width.
fig1.bar(china_citynames,china_cities,0.5)
fig2.bar(uk_citynames,uk_cities,0.5)
#label the figs with city and population
fig1.set_xlabel('City')
fig1.set_ylabel('Population')
fig2.set_xlabel('City')
fig2.set_ylabel('Population')
plt.show()