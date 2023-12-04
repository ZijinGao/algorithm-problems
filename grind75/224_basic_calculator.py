class Solution:
    def parse(self, s: str) -> List[int]:
        s_list = []
        idx = 0
        while idx < len(s):
            if not s[idx].isspace():
                if s[idx] == '+' or s[idx] == '-' or s[idx] == '(' or s[idx] == ')':
                    s_list.append(s[idx])
                    idx += 1
                elif s[idx].isnumeric():
                    num = 0
                    while idx < len(s) and s[idx].isnumeric():
                        num = num * 10 + int(s[idx])
                        idx += 1
                    s_list.append(str(num))
            else:
                idx += 1
        return s_list

    def calculate(self, s: str) -> int:
        s_list = self.parse(s)        
        stack = []

        for char in s_list:
            if char == ")":
                temp_exp = []
                while stack[-1] != "(":
                    temp_exp.append(stack.pop())
                stack.pop() # pop the remaining "("
                temp_exp = temp_exp[::-1]
                if temp_exp[0] == '+' or temp_exp[0] == "-":
                    temp_exp = ['0'] + temp_exp[:]
                temp_res = int(temp_exp[0])
                for i in range(1, len(temp_exp), 2):
                    if temp_exp[i] == '+':
                        temp_res += int(temp_exp[i+1])
                    else:
                        temp_res -= int(temp_exp[i+1])
                stack.append(temp_res)
            else:
                stack.append(char)
                
        if stack[0] == '-' or stack[0] == '+':
            stack = ["0"] + stack[:]
        res = int(stack[0])
        for i in range(1, len(stack), 2):
            if stack[i] == '+':
                res += int(stack[i+1])
            else:
                res -= int(stack[i+1])
        return res
