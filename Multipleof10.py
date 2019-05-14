def round(num):
a=(num//10)*10
b=a+10
return(b if num- a>b - num else a)
num=int(input("Enter a number"))
print(round(num))
