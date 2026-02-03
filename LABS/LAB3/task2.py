def us(x):
    while (x%2==0 or x%3==0 or x%5==0):
        if (x%2==0):
            x=int(x/2)
        if (x%3==0):
            x=int(x/3)
        if (x%5==0):
            x=int(x/5)
    if x==1:
        return "Yes"
    else:
        return "No"

x=int(input())
print(us(x))