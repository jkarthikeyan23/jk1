n=int(input("enter the number"))
sum=0
while(n>0):
reminder=n%10
sum=sum+reminder
n=n//10
print("the sum of digits",sum)
