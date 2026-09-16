class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        largest = 0

        while l <= r:
            v = min(heights[l], heights[r]) * (r - l)
            largest = max(v, largest)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return largest


        