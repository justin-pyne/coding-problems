# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        q = deque([node])
        clones = {node: Node(node.val)}

        while q:
            curr = q.popleft()
            curr_clone = clones[curr]

            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                
                curr_clone.neighbors.append(clones[neighbor])
        
        return clones[node]