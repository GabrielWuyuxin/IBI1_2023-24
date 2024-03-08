#let a be the density at the beginning, let s be 0 referring to day1, so on day2 s will be 1.
#every time when one day pasts, the density doubles.
#when a reach 0.9, s refers to the number of the day that you can go out for break.
a=0.05
s=0
while a<=0.9:
    a*=2
    s+=1
print("The day can leave="+str(s))
