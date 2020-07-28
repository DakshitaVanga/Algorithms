#Longest common Subsequence

#Recursive

def lcs(x,y,m,n):
	if m==0 or n==0:
		return 0
	elif x[m-1]==y[n-1]:
		if x[m-1] not in l1:
			l1.append(x[m-1])
		return 1+lcs(x,y,m-1,n-1)
	else:
		return max(lcs(x,y,m-1,n),lcs(x,y,m,n-1))

x=input("Enter string 1: ")
y=input("Enter string 2: ")
m=len(x)
n=len(y)
l1=[]
res=lcs(x,y,m,n)
print(res)
print(l1)