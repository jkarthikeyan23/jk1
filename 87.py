n,k=map(int,input().split())
if n>k:
x=n
else
x=k
for i in range(1,x+1):
	if n%i==0 and m%i==0:
		d=i
print(d)
