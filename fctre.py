from __future__ import division, print_function
import bisect
import math
import heapq
import itertools
import sys
from collections import deque
from atexit import register
from collections import Counter
from functools import reduce
sys.setrecursionlimit(10000000)
if sys.version_info[0] < 3:
    from io import BytesIO as stream
else:
    from io import StringIO as stream
 
 
if sys.version_info[0] < 3:
    class dict(dict):
        """dict() -> new empty dictionary"""
        def items(self):
            """D.items() -> a set-like object providing a view on D's items"""
            return dict.iteritems(self)
 
        def keys(self):
            """D.keys() -> a set-like object providing a view on D's keys"""
            return dict.iterkeys(self)
 
        def values(self):
            """D.values() -> an object providing a view on D's values"""
            return dict.itervalues(self)
 
    input = raw_input
    range = xrange
 
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip
 
 
def sync_with_stdio(sync=True):
    """Set whether the standard Python streams are allowed to buffer their I/O.
 
    Args:
        sync (bool, optional): The new synchronization setting.
 
    """
    global input, flush
 
    if sync:
        flush = sys.stdout.flush
    else:
        sys.stdin = stream(sys.stdin.read())
        input = lambda: sys.stdin.readline().rstrip('\r\n')
 
        sys.stdout = stream()
        register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))
        
def main():
    import Queue
    import math  
    m=1000000007
    def printDivisors(n) :
    	cnt=0
    	i = 1
    	while i <= math.sqrt(n): 
    			
    		if (n % i == 0) : 
    				
    			if (n / i == i) : 
    				cnt=(cnt+1)%m 
    			else : 
    				cnt=(cnt+2)%m
    		i = i + 1
    	return cnt
    
    
    def minEdgeBFS(edges, u, v, n, cost):
    	temp=cost.copy()
    
    	visited = [0] * n
    
    	distance = [0] * n
    
    	Q = queue.Queue()
    	distance[u] = 0
    
    	Q.put(u)
    	visited[u] = True
    	while (not Q.empty()):
    		x = Q.get()
    
    		for i in range(len(edges[x])):
    			if (visited[edges[x][i]]):
    				continue
    
    			distance[edges[x][i]] = distance[x] + 1
    			temp[edges[x][i]]*=temp[x]
    			
    			Q.put(edges[x][i])
    			visited[edges[x][i]] = 1
    			
    	return temp[v]
    
    
    def addEdge(edges, u, v):
    	edges[u].append(v)
    	edges[v].append(u)
    
    # # Driver Code
    # if __name__ == '__main__':
    
    #     # To store adjacency list of graph
    #     n = 9
    #     edges = [[] for i in range(n)]
    #     addEdge(edges, 0, 1)
    #     addEdge(edges, 0, 7)
    #     addEdge(edges, 1, 7)
    #     addEdge(edges, 1, 2)
    #     addEdge(edges, 2, 3)
    #     addEdge(edges, 2, 5)
    #     addEdge(edges, 2, 8)
    #     addEdge(edges, 3, 4)
    #     addEdge(edges, 3, 5)
    #     addEdge(edges, 4, 5)
    #     addEdge(edges, 5, 6)
    #     addEdge(edges, 6, 7)
    #     addEdge(edges, 7, 8)
    #     u = 0
    #     v = 5
    #     print(minEdgeBFS(edges, u, v, n))
    
    
    # # This code is contributed by PranchalK
    t = int(input())
    while t:
    	t -= 1
    	n = int(input())
    	cost=[]
    	
    	edges = [[] for i in range(n)]
    
    	for i in range(n-1):
    		a, b = map(int, input().split())
    		addEdge(edges, a-1, b-1)
    
    	dist = list(map(int, input().split()))
    
    	for i in range(n):
    		cost.append(dist[i])
    
    	k = int(input())
    	ans = []
    	for i in range(k):
    		u, v = map(int, input().split())
    		print(printDivisors(minEdgeBFS(edges, u-1, v-1, n, cost)))

        

if __name__ == '__main__':
    sync_with_stdio(False)
    main()
