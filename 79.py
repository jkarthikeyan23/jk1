import math
s1,k=map(int,raw_input().split())
p=s1*k
if math.sqrt(p).is_integer():
    print "yes"
else:
    print "no"
