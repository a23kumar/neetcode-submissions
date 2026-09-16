from collections import defaultdict
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # n == number of nodes in the graph
        # edges: for of [u, v, w]: u == source node, v == destination node, w == weight of the edge
        # All nodes are labled with values from 0 to n - 1
        # src == the source node to start the algorithm
        adj = defaultdict(list)
        
        for s, d, weight in edges:
            adj[s].append([d, weight])

        shortest = {} # Map vertex, distance of shortest path
        minheap = [[0, src]] # from the source node, the cost is 0, to reach the source node
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minheap, [w1 + w2, n2])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest

