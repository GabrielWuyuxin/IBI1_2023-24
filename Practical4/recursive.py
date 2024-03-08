#let begin value a be 0.5, represents the "a0", so that the first "a" after caculation, which is 4, becomes "a1".
#i represents the ordinal number, when i adds 1, a is caculated as multiple by 2 and add 3.
a=0.5
i=1
for i in range(1,6,1):#the 6 can be changed if we want more munber to be printed
    a=2*a+3
    print(a)
