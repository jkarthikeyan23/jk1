lst=[]
number=int(input('how many numbers:'))
for n in range(number):
num=int(input('enter number'))
lst.append(num)
print("maximum element in the list is :",max(lst),"\nminimum element in the list is :",min(lst))
