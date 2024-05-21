x=input('You were born in:')
def favourite_jamesbond(x):
    """input=the year you were born
    output=the james bomd you saw when you were 18 years old
    """
    x=int(x)+18
    y={1:"Roger Moore",2:"Timothy Dalton",3:"Pierce Brosnan",4:"Daniel Craig"}
    if 1973<=x<=1986:
        favourite_jamesbond=y[1]
    elif 1987<=x<=1994:
        favourite_jamesbond=y[2]
    elif 1995<=x<=2005:
        favourite_jamesbond=y[3]
    elif 2006<=x<=2021:
        favourite_jamesbond=y[4]
    else:
        favourite_jamesbond="There's no favourite james bond!"
    return "Your favourite james bond is:",(favourite_jamesbond)
print (favourite_jamesbond(x))
