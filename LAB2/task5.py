x=int(input())
y=2
c=False
while(y<=x):
    if(y==x):
        c=True
        break
    y*=2
if(c):
    print("YES")
else:
    print("NO")

    