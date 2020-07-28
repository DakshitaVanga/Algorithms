#Longest common Subsequence

#Memoization

def lcs(x,y,m,n):
	if m==0 or n==0:
		dp[m][n]=0
		return dp[m][n]
	if dp[m][n]!=-1:
		return dp[m][n]
	elif x[m-1]==y[n-1]:
		if x[m-1] not in l1:
			l1.append(x[m-1])
		dp[m][n]= 1+lcs(x,y,m-1,n-1)
		return dp[m][n]
	else:
		dp[m][n]=max(lcs(x,y,m-1,n),lcs(x,y,m,n-1))
		return dp[m][n]

x=input("Enter string 1: ")
y=input("Enter string 2: ")
m=len(x)
n=len(y)
l1=[]
dp=[[-1 for i in range(n+1)] for j in range(m+1 )]
res=lcs(x,y,m,n)
print(res)
print(l1)
l1.reverse()
print(dp)