class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        # (10 - 1) / 3 = 3
        # = (10 - 4) / 2 = 3

        # (10 - 4) / 2 = 3
        # (10 - 1) / 2 = 5
        # (10 - 0) / 1 = 10
        # (10 - 7) / 3 = 1

        # formula: (target - position) // speed

        stack = []
        pairs = [(pos, speed) for pos, speed in zip(position, speed)]
        pairs.sort(reverse=True)

        for p, s in pairs:
            steps = (target - p) / s
            stack.append(steps)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)