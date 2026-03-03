n=int(input())
mas=list(map(int,input().split()))
cnt=0
for i in range(n):
    if mas[i]!=0:
        cnt+=1

print(cnt)