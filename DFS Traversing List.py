from collections import defaultdict
graph=defaultdict(list)
v,e=map(int,input().split())
for i in range(e):
    u,v = map(str,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph,start,visited,path):
    path.append(start)
    visited[start]=True
    for i in graph[start]:
        if visited[i]==False:
            dfs(graph,i,visited,path)
    return path

path=[]
start='A'
visited= defaultdict(bool)
traversedpath=dfs(graph,start,visited,path)
print(traversedpath)

'''
5 5
A B
A D
A C
C E
C D
'''
