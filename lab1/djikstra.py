from dimacs import *
from queue import PriorityQueue

def E_to_V(E,n):
    V = [ [] for _ in range((n+1)) ]
    for u,v,w in E:
        V[u].append((v,w))
        V[v].append((u,w))
    return V

def djikstra(V,s,n):
    minmax = [ None ] * (n+1)
    q = PriorityQueue()
    for v,w in V[s]:
        q.put((-w,v))
        minmax[v] = w
    while not q.empty():
        w,u = q.get()
        w = -w
        w = min(w, minmax[u])
        for v,w1 in V[u]:
            w1 = min(w,w1)
            if minmax[v] is None:
                minmax[v] = w1
                q.put((-w1,v))
            if w1 > minmax[v]:
                minmax[v] = w1 
                q.put((-w1,v))
    return minmax

def run(filename, mode=0):
    (V,L) = loadWeightedGraph(filename)

    v = E_to_V(L,V)
    # print(v)
    s = 1
    t = 2
    if mode == 0:
        s = int(input(f"Starting vertex no (0-{V}):"))
        t = int(input(f"End verted no (0-{V}): "))
    minmax_path = djikstra(v,s,V)
    if V < 20:
        print(minmax_path)
    print(f"{filename} {minmax_path[t]}")

table = [
"clique100",
"clique1000",
"clique20",
"clique5",
"g1",
"grid100x100",
"grid5x5",
"path10",
"path1000",
"path10000",
"pp10",
"pp100",
"pp1000",
"rand1000_100000",
"rand100_500",
"rand20_100"]
for element in table:
    run("./tests/" + element,1)
