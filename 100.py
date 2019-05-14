s=int(raw_input())
pro=1
while s>0:
    dig=s%10
    pro=pro-dig
    s=s/10
print pro
