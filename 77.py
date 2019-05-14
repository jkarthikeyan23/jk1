m=int(input(""))
l=[]
for i in range(1,k+1):
  if k%i==0:
    l.append(i)
print(*l,end="")
