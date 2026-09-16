from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        # We can map out these relationships in a hashmap
        mappings = defaultdict(list)
        visit = set()
        # we can then get all of 
        for x, y in edges:
            mappings[x].append(y)
            mappings[y].append(x)
        
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)

            for v in mappings[i]:
                if v == prev:
                    continue

                if not dfs(v, i):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visit)
                