def val(x):
    while(x>0):
        a=x%10
        if a%2!=0:
            return "Not valid"
        x=int(x/10)
    return "Valid"

x=int(input())
print(val(x))