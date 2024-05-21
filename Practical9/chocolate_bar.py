#x=input("Your money is:")
#y=input("The price of one chocolate bar is:")
def chocolate_bar(x,y):
    number=int(x)//int(y)
    money_left=int(x)%int(y)
    return("You can buy ",str(number),"chocolate bars with ",str(money_left),"yuan left")
print(chocolate_bar(100,6))