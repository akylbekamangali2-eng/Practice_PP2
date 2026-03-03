n=int(input())
w=list(map(str,input().split()))
maxi=w[0]
for elem in w:
    cur=elem
    if len(cur)>len(maxi):
        maxi=cur

print(maxi)