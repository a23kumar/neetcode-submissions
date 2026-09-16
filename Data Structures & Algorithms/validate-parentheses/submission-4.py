class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        mappings = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for val in s:
            if val == '(' or val == '{' or val == '[':
                stack.append(val)
            else:
                if stack and stack[len(stack) - 1] == mappings[val]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False