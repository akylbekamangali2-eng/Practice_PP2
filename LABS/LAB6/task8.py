n=int(input())
mas=list(map(int,input().split()))
a=set(mas)
for elem in sorted(a):
    print(elem,end=" ")
