def check_power(n,k):
if n<=0 or k<=0:
print "not valid input"
else:
for i in range(1,18):
x=k**i
if x==n:
print"true"
print k,"power","is",n
break
elif
print "false"
break
check_power(244140625,5)
check_power(4096,16)
check_power(0,16)
check_power(1,1)
