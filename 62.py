a=str(input())
count=0
for i in range (0,len(a)):
	if a[i]=="1" or a[i]=="2":
		count=count+1
	else:
		count=count+2
if count==0:
	print("yes")
else:
	print("no")
	
''' binARY OR nOT
'''
