n=int(input())
keys=input().split()
values=input().split()
s=input()
a={}
for i in range(n):
    a[keys[i]]=values[i]

if s in keys:
    print(a[s])
else:
    print("Not found")