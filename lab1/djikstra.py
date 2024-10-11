from dimacs import *
from queue import PriorityQueue

def E_to_V(E,n):
    V = [ [] for _ in range((n+1)) ]
    for u,v,w in E:
        V[u].append((v,w))
        V[v].append((u,w))
    return V

def djikstra(V,s,n):
    minmax = [ 0 ] * (n+1)
    q = PriorityQueue()
    q.put((0,s))
    while not q.empty():
        w,u = q.get()
        w = -w
        w = min(w, minmax[u])
        for v,w1 in V[u]:
            w1 = min(w,w1)
            if w1 > minmax[v]:
                minmax[v] = w1 
                q.put((-w1,v))
    return minmax

(V,L) = loadWeightedGraph("clique5")

v = E_to_V(L,V)
print(v)
s = int(input(f"Starting vertex no (0-{V}):"))
t = int(input(f"End verted no (0-{V}): "))
minmax_path = djikstra(v,s,V)
print(minmax_path)
print(minmax_path[t])
