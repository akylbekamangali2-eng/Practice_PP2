n=int(input())
mas=list(map(int,input().split()))
flag=True
for i in range(n):
    if mas[i]<0:
        flag=False
        break
    
if flag:
    print("Yes")
else:
    print("No")