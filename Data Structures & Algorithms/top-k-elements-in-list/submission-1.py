class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            hm[n] += 1
        
        
        for n, f in hm.items():
            freq[f].append(n)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            res += freq[i]
            if len(res) == k:
                return res