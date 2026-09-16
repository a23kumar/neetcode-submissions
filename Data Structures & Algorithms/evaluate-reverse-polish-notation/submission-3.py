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
                b = stack.pop()
                a = int(stack.pop())

                stack.append(int(opps[v](a,b)))
            else:
                stack.append(int(v))
        return stack[-1]