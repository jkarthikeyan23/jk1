def findK(n,z): 
    half=int((n+1)/2) 
    if z>n: 
        return(2+(z-half)) 
    else: 
        return(2+z - 1) 
n=5
z=3
print(findK(n,z)) 
