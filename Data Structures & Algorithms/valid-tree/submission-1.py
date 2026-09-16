from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        mappings = defaultdict(list)
        visit = set()
        for n1, n2 in edges:
            mappings[n1].append(n2)
            mappings[n2].append(n1)

        def dfs(n1, prev):
            if n1 in visit:
                return False
            visit.add(n1)
            for i in mappings[n1]:
                if i == prev:
                    continue
                if not dfs(i, n1):
                    return False
            return True


        return dfs(0, -1) and n == len(visit)
