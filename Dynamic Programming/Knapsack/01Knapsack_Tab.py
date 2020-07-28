#0/1 Knapsack Problem

#Tabulation i.e Bottom Up
'''
Compute all the values
'''

n=int(input("Enter number of items: "))
w=list(map(int,input("Enter weight of each item: ").split()))
val=list(map(int,input("Enter value of each item: ").split()))
W=int(input("Enter capacity: "))
dp = [[-1 for x in range (W+1)] for y in range(n+1)] 
print("n: ",n,"W: ",W)
print("w: ",w)
print("Val: ",val)
print("Matrix: ")

for i in range(0,n+1):
	for j in range(0,W+1):
		if i==0 or j==0:
			dp[i][j]=0

for i in range(1,n+1):
	for j in range(1,W+1):
		if w[i-1]<=j:
			dp[i][j]=max(val[i-1]+dp[i-1][j-w[i-1]],dp[i-1][j])
		else:
			dp[i][j]=dp[i-1][j]

for i in range(0,n+1):
	print(dp[i])