class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        valid_signs = ["+", "-", "*", "/"]

        for t in tokens:
            if t in valid_signs:
                b = stack.pop()
                a = stack.pop()
                match t:
                    case "+":
                        new = a + b
                    case "-":
                        new = a - b
                    case "*":
                        new = a * b
                    case "/":
                        new = int(a / b)
                    
                stack.append(new)
            else:
                stack.append(int(t))

        return stack[0]