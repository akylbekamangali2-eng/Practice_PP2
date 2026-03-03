n=int(input())
a=list(map(int,input().split()))
mas=filter(lambda x:x%2==0,a)
print(len(mas))