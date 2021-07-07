parents = range(n)
ranks = [0] * n

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    xroot = find(x)
    yroot = find(y)
    if xroot == yroot: return
    if ranks[x] < ranks[y]:
        xroot, yroot = yroot, xroot
    parent[yroot] = xroot
    ranks[xroot] = max(ranks[xroot], ranks[yroot] + 1)
    
    
    
    
for i in range(n):
    if is_connected(x, y):
        union(x, y)
    
