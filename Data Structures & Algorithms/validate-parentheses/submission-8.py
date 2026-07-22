class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        stack = []

        for char in s:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if len(stack) < 1:
                    return False

                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False

        if stack:
            return False

        return True