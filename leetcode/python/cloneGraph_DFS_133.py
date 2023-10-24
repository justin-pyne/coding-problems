
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        def dfs(node, graph):
            if node not in graph:
                graph[node] = Node(node.val)
                for neighbor in node.neighbors:
                    graph[node].neighbors.append(dfs(neighbor, graph))
            return graph[node]
        
        return dfs(node, {None: None})