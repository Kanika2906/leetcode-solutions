class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for char in tokens:
            if char not in "+-*/":
                stack.append(int(char))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if char =="+":
                    stack.append(op1+op2)
                elif char =="-":
                    stack.append(op1-op2)
                elif char =="*":
                    stack.append(op1*op2)
                else:
                    stack.append(int(op1/op2))
                
        return (stack[-1])
        