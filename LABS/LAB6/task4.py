n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
scal=0
for i in range(n):
    scal+=a[i]*b[i]

print(scal)
