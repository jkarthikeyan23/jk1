m=int(input())
z=[int(i) for i in input().split()]
for i in range(1,m):
    if((i+1)!=z[i]):
        print(i)
        break
