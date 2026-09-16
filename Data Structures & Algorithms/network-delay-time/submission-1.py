from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # n nodes labled 1 - n
        # directed graph
        # Given list times - time[i] = (i1, v1, ti)
        # --- ui is source node (integer 1-n)
        # ---- vi is target node (integer 1-n)
        # ---- ti is time it takes for a signal to travel from source to target node (>= 0)

        # we are also given a source node (k) where the signal will be sent from


        # we need djikstras algorithm

        #1. Create adjacency list
        adj = defaultdict(list)

        for s, time, target in times:
            adj[s].append([time, target])

        minheap = [(0, k)]
        seen = set()
        x = 0 # this keep track of the current best time
        while minheap:
            t, node = heapq.heappop(minheap) # t = time, n = node
            if node in seen:
                continue
            seen.add(node)
            x = t # by the end this would have the total time of the shortest path
            for n2, t2 in adj[node]:
                if n2 not in seen:
                    heapq.heappush(minheap, (t + t2, n2))
        
        return x if len(seen) == n else -1
