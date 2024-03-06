#a=density at the beginning, s on day1 =0
#every time a=a*2,s=s+1
a=0.05
s=0
while a<=0.9:
    a*=2
    s+=1
print("The day can leave="+str(s))