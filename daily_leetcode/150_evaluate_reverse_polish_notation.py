class Solution:
    def evalRPN(self, token: list[str]) -> int:
        stack = []
        for t in token:
            if t not in {"+", "-", "/", "*"}:
                stack.append(float(t))
            else:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                if t == "+":
                    stack.append(n1 + n2)
                elif t == "-":
                    stack.append(n1 - n2)
                elif t == "*":
                    stack.append(n1 * n2)
                elif t == "/":
                    stack.append(n1 / n2)
        return int(stack[0])