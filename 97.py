z=int(raw_input())
rev=0
while(z>0):
    dig=z%10
    rev=rev+10+dig
    z=z//10
print(rev)
