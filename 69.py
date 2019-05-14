class ifoddeve:
	def sub(self,j,k):
		s=j-k
		s=abs(s)
		if s%2==0:
			print("even")
		else:
			print("odd")
n,j=map(int,input().split())
call=ifoddeve()
call.sub(n,j)
