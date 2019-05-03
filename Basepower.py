import math
def Log2(a):
    if a==0:
      return false;
    return (math.log10(a) /
            math.log10(2));
def isPowerOfTwo(n):
    return (math.ceil(Log1(n)) ==
            math.floor(Log2(n)));
if(isPowerOfTwo(31)):
    print("YES");
else:
    print("NO");
if(isPowerOfTwo(64)):
    print("YES");
else:
    print("NO");
