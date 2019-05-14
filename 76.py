m1=int(raw_input())
factor=0
for i in range(1,k1):
  if k1%i==0:
    factor=i
if factor>1:
  print "yes"
elif k1==1:
  print "prime"
else:
  print "no"
