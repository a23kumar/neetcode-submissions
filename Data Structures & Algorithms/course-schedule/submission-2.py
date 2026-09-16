from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mappings = defaultdict(list)

        visit = set()

        for c, pre in prerequisites:
            mappings[c].append(pre)

        
        def dfs(c):
            if c in visit:
                return False
            if mappings[c] == []:
                return True
            visit.add(c)

            for i in mappings[c]:
                if not dfs(i): return False
            
            visit.remove(c)
            mappings[c] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        return True
            