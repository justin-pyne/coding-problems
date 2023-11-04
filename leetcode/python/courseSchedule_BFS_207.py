from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adj list & indegree
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # create adj list
        for prereq, course in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        
        # create queue
        q = deque([course for course in range(numCourses) if indegree[course] == 0])

        # bfs
        completed = 0
        while q:
            course = q.popleft()
            completed += 1

            for next_course in adj[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)
        
        return completed == numCourses
