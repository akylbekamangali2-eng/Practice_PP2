x=int(input())
y=map(int,input().split())
s=0
for i in y:
    if(i>0):
        s+=1
print(s)