from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adj list, visited array
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        # build adj list
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        res = []


        def dfs(course):
            # base cases
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            
            # update visited
            visited[course] = 1

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            
            visited[course] = 2
            res.append(course)
            return True
        
        for course in range(numCourses):
            if visited[course] == 0:
                if not dfs(course):
                    return []
        
        return res[::-1]
