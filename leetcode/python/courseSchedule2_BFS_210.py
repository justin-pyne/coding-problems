from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        bfs topological sort (kahns algo)
        """
        # adj list
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # build adj list
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        # build queue
        q = deque([course for course in range(numCourses) if indegree[course] == 0])

        res = []
        taken = 0
        while q:
            course = q.popleft()
            taken += 1
            res.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)

        return res if taken == numCourses else []
