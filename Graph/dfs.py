#Depth First Search

'''
Enter number of nodes: 6
Enter node: A
Enter list: B,C
Enter node: B
Enter list: D,E
Enter node: C
Enter list: F
Enter node: D
Enter list:
Enter node: E
Enter list: F
Enter node: F
Enter list:
{'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}
Enter Start node: A
Path is:  ABDEFC
'''

def dfs(visited,graph,node):
	if node not in visited:
		visited.add(node)
		l.append(node)
		for nxt in graph[node]:
			dfs(visited,graph,nxt)

n=int(input("Enter number of nodes: "))
graph=dict()
for i in range(n):
	x=input("Enter node: ")
	graph[x]=list(input("Enter list: ").strip().split(','))

visited=set()

for i in graph:
	if graph[i]==['']:
		graph[i]=[]
l=[]
print(graph)
start_node=input('Enter Start node: ')
dfs(visited,graph,start_node)
path=''.join(l)
print("Path is: ",path)