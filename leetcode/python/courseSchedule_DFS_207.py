from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        # create adj list
        for prereq, course in prerequisites:
            graph[course].append(prereq)


        def dfs(course):
            if visited[course] == 1: # processing -> loop
                return False
            if visited[course] == 2: # processed -> safe
                return True
            
            # update visited
            visited[course] = 1
            
            # dfs prereqs
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            visited[course] = 2
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
