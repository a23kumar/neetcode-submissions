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
        print(adj)
        shortest = {} # We are mapping a vertex -> the shortest path
        minheap = [[0, src]] # from the source node, the cost is 0, to reach the source node
        while minheap:
            w1, n1 = heapq.heappop(minheap) # we get the weight and the node
            if n1 in shortest: # if we have already seen this node, we can just go to the next iteration
                continue
            shortest[n1] = w1 # Maps the total distance it takes to get this this node
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minheap, [w1 + w2, n2])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        return shortest

