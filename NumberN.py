def findnext(number,n):
for i in range(n-1,0,-1):
if number[i]>number[i-1]:
break
if i==0:
print"next number not possible"
retun
x=number[i-1]
smallest=i
for j in range(i+1,n):
if number[j]>x and number[j]<number[smallest]:
smallest=j
number[smallest],number[i-1]=number[i-1],number[smallest]
x=0
for j in range(i):
x=x*10+number[j]
number=sorted(number[i:])
for j in range(n-i):
x=x*10+number[j]
print"next number with set of digits is",x
digits="534976"
number=map(int,digits)
findnext(number,len(digits))
