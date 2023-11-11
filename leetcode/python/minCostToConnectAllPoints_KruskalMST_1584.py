from typing import List


class UnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, n):
        if n != self.par[n]:
            self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        create a list of tuples with distance between two points (weighted edges)
        sort list by weights
        iterate through weighted edges, if doesnt create a cycle, union
        count numEdges, update cost
        if numEdges is n-1, break out and return cost
        """

        n = len(points)
        if n == 1:
            return 0


        edges = []
        for i in range(n):
            xi, yi = points[i]
            for j in range(i+1, n):
                xj, yj = points[j]
                manhattan = abs(xi-xj) + abs(yi-yj)
                edges.append((manhattan, i, j))
        edges.sort()

        numEdges = 0
        cost = 0
        dsu = UnionFind(n)
        for manhattan, i, j in edges:
            if dsu.find(i) != dsu.find(j):
                dsu.union(i, j)
                cost += manhattan
                numEdges += 1
                if numEdges == n-1:
                    return cost

        