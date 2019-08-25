# PT07Y - Is it a tree

n,m = map(int, input().split())
adj = dict()
for _ in range(m):
    x,y = map(int, input().split())
    if x in adj:
        adj[x].append(y)
    else:
        adj[x] = [y]
    if y in adj:
        adj[y].append(x)
    else:
        adj[y] = [x]

def dfs(vertex):
    visited.add(vertex)
    for node in adj[vertex]:
        if node not in visited:
            dfs(node)

if m != n-1:
    print('NO')
else:
    visited = set()
    dfs(1)
    if len(visited) == n:
        print('YES')
    else:
        print('NO')
    