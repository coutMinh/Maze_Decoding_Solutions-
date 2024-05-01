import numpy as np
import heapq as pq
maxn = 100001
INF = 1e9
matrix = np.array([['o','x','o','o','o'],
                   ['o','x','o','x','x'],
                   ['o','x','o','x','x'],
                   ['o','o','o','x','x'],
                   ['o','o','o','x','x']])
n = len(matrix)
sx = 0
sy = 0
dx = [-1,0,0,1]
dy = [0,-1,1,0]
step = np.array([[INF for i in range(n)] for j in range(n)])
step[sx, sy] = 0
Q = []
pq.heappush(Q, (0, (sx, sy)))
while(Q):
    top = pq.heappop(Q)
    kc = top[0]
    u = top[1]
    i = u[0]
    j = u[1]
    if(kc > step[u]): continue
    for k in range(4):
        newi = i + dx[k]
        newj = j + dy[k] 
        w = None
        if(newi >= 0 and newi < n) and (newj < n and newj >= 0) :
            if(matrix[newi, newj] == 'x'):
                w = INF
            else: w = 1
            if(step[newi, newj] > step[u] + w):
                step[newi, newj] = step[u] + w
                pq.heappush(Q, (step[newi, newj], (newi, newj)))

print(step)
                