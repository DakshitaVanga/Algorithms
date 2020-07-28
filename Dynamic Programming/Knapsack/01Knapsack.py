#0/1 Knapsack Problem

#Memoization i.e Top Down
'''
Dont compute all the values
'''

def knapsack(w,val,W,n):
	if n==0 or W==0:
		return 0
	if dp[n][W]!=-1:
		return dp[n][W]
	elif w[n-1]<=W:
		dp[n][W]=max(val[n-1]+knapsack(w,val,W-w[n-1],n-1),knapsack(w,val,W,n-1))
		return dp[n][W]
	else:
		dp[n][W]=knapsack(w,val,W,n-1)
		return dp[n][W]

n=int(input("Enter number of items: "))
w=list(map(int,input("Enter weight of each item: ").split()))
val=list(map(int,input("Enter value of each item: ").split()))
W=int(input("Enter capacity: "))
dp = [[-1 for x in range (W+1)] for y in range(n+1)] 
print("n: ",n,"W: ",W)
print("w: ",w)
print("Val: ",val)

wt=W
res=knapsack(w,val,W,n)
print(res)


