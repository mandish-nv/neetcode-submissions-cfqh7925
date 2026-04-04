class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = "[{()}]"
        opening = "[{("
        closing = ")}]"
        for char in s:
            if char not in valid:
                return False
            
            if len(stack) == 0 or char in opening:
                stack.append(char)
            else:
                match char:
                    case ")":
                        if stack[-1] == "(":
                            stack.pop()
                        else:
                            return False
                    case "}":
                        if stack[-1] == "{":
                            stack.pop()
                        else:
                            return False
                    case "]":
                        if stack[-1] == "[":
                            stack.pop()
                        else:
                            return False
        
        if len(stack) == 0:
            return True
        else:
            return False
            

            