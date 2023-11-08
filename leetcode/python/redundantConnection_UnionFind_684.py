from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [0] * (len(edges) + 1)

        def find(n):
            # returns the root node of a tree
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            # return false if already union, return true if successful
            p1, p2 = find(n1), find(n2)

            if p1 == p2: # same tree
                return False # cannot union same tree

            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p1] < rank[p2]:
                par[p1] = p2
            else:
                par[p2] = p1
                rank[p1] += 1
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]