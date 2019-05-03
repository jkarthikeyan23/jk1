number=int(input('how many numbers:'))
total_sum=0
for n in range(number):
numbers=float(input('enter number'))
total_sum+=numbers
avg=total_sum/number
print('average of',number,'numbers is :',avg)
