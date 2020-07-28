#Longest common Subsequence

#Tabulation

x=input("Enter string 1: ")
y=input("Enter string 2: ")
m=len(x)
n=len(y)
l1=[]
dp=[[-1 for i in range(n+1)] for j in range(m+1 )]

for i in range(0,m+1):
	for j in range(0,n+1):
		if i==0 or j==0:
			dp[i][j]=0
		elif x[i-1]==y[j-1]:
			dp[i][j]= 1+dp[i-1][j-1]
		else:
			dp[i][j]=max(dp[i-1][j],dp[i][j-1])

res=dp[m][n]
print(res)
for i in dp:
	print(i)

i=m
j=n
while i>0 and j>0:
	if x[i-1]==y[j-1]:
		l1.append(x[i-1])
		i-=1
		j-=1
	else:
		if dp[i][j-1]>dp[i-1][j]:
			j-=1
		else:
			i-=1

res=''.join(l1)
print(res[::-1])