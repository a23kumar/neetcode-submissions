import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opps = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        stack = []

        for v in tokens:
            if v in opps:
                b = int(stack.pop())
                a = int(stack.pop())

                stack.append(opps[v](a,b))
            else:
                stack.append(int(v))
        return int(stack[-1])