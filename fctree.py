from collections import deque 
from math import log2 
  
MAX = 100001
  
# A tree node structure 
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
# Array to store level of each node 
level = [0] * MAX
  
# Utility Function to store level of all nodes 
def findLevels(root: Node): 
    global level 
  
    if root is None: 
        return
  
    # queue to hold tree node with level 
    q = deque() 
  
    # let root node be at level 0 
    q.append((root, 0)) 
  
    # Do level Order Traversal of tree 
    while q: 
        p = q[0] 
        q.popleft() 
  
        # Node p.first is on level p.second 
        level[p[0].data] = p[1] 
  
        # If left child exits, put it in queue 
        # with current_level +1 
        if p[0].left: 
            q.append((p[0].left, p[1] + 1)) 
  
        # If right child exists, put it in queue 
        # with current_level +1 
        if p[0].right: 
            q.append((p[0].right, p[1] + 1)) 
  
# Stores Euler Tour 
Euler = [0] * MAX
  
# index in Euler array 
idx = 0
  
# Find Euler Tour 
def eulerTree(root: Node): 
    global Euler, idx 
    idx += 1
  
    # store current node's data 
    Euler[idx] = root.data 
  
    # If left node exists 
    if root.left: 
  
        # traverse left subtree 
        eulerTree(root.left) 
        idx += 1
  
        # store parent node's data 
        Euler[idx] = root.data 
  
    # If right node exists 
    if root.right: 
  
        # traverse right subtree 
        eulerTree(root.right) 
        idx += 1
  
        # store parent node's data 
        Euler[idx] = root.data 
  
# checks for visited nodes 
vis = [0] * MAX
  
# Stores level of Euler Tour 
L = [0] * MAX
  
# Stores indices of the first occurrence 
# of nodes in Euler tour 
H = [0] * MAX
  
# Preprocessing Euler Tour for finding LCA 
def preprocessEuler(size: int): 
    global L, H, vis 
    for i in range(1, size + 1): 
        L[i] = level[Euler[i]] 
  
        # If node is not visited before 
        if vis[Euler[i]] == 0: 
  
            # Add to first occurrence 
            H[Euler[i]] = i 
  
            # Mark it visited 
            vis[Euler[i]] = 1
  
# Sparse table of size [MAX][LOGMAX] 
# M[i][j] is the index of the minimum value in 
# the sub array starting at i having length 2^j 
M = [[0 for i in range(18)] for j in range(MAX)] 
  
# Utility function to preprocess Sparse table 
def preprocessLCA(N: int): 
    global M 
    for i in range(N): 
        M[i][0] = i 
  
    j = 1
    while 1 << j <= N: 
        i = 0
        while i + (1 << j) - 1 < N: 
            if L[M[i][j - 1]] < L[M[i + 
                (1 << (j - 1))][j - 1]]: 
                M[i][j] = M[i][j - 1] 
            else: 
                M[i][j] = M[i + (1 << (j - 1))][j - 1] 
            i += 1
        j += 1
  
# Utility function to find the index of the minimum 
# value in range a to b 
def LCA(a: int, b: int) -> int: 
  
    # Subarray of length 2^j 
    j = int(log2(b - a + 1)) 
    if L[M[a][j]] <= L[M[b - (1 << j) + 1][j]]: 
        return M[a][j] 
    else: 
        return M[b - (1 << j) + 1][j] 
  
# Function to return distance between 
# two nodes n1 and n2 
def findDistance(n1: int, n2: int) -> int: 
  
    # Maintain original Values 
    prevn1 = n1 
    prevn2 = n2 
  
    # Get First Occurrence of n1 
    n1 = H[n1] 
  
    # Get First Occurrence of n2 
    n2 = H[n2] 
  
    # Swap if low>high 
    if n2 < n1: 
        n1, n2 = n2, n1 
  
    # Get position of minimum value 
    lca = LCA(n1, n2) 
  
    # Extract value out of Euler tour 
    lca = Euler[lca] 
  
    # return calculated distance 
    return level[prevn1] + level[prevn2] - 2 * level[lca] 
  
def preProcessing(root: Node, N: int): 
  
    # Build Tree 
    eulerTree(root) 
  
    # Store Levels 
    findLevels(root) 
  
    # Find L and H array 
    preprocessEuler(2 * N - 1) 
  
    # Build sparse table 
    preprocessLCA(2 * N - 1) 
  
# Driver Code 
if __name__ == "__main__": 
  
    # Number of nodes 
    N = 8
  
    # Constructing tree given in the above figure 
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    root.right.left = Node(6) 
    root.right.right = Node(7) 
    root.right.left.right = Node(8) 
  
    # Function to do all preprocessing 
    preProcessing(root, N) 
  
    print("Dist(4, 5) =", findDistance(4, 5)) 
    print("Dist(4, 6) =", findDistance(4, 6)) 
    print("Dist(3, 4) =", findDistance(3, 4)) 
    print("Dist(2, 4) =", findDistance(2, 4)) 
    print("Dist(8, 5) =", findDistance(8, 5)) 