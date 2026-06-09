from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = deque()
        for i in range(len(tokens)):

            if tokens[i] in "+-*/":
                a = stk.pop()
                b = stk.pop()
                if tokens[i] == "+":
                    stk.append(b+a)
                elif tokens[i] == "-":
                    stk.append(b-a)
                elif tokens[i] == "*" :
                    stk.append(b*a)
                else:
                    stk.append(int(b/a))
            else:
                stk.append(int(tokens[i]))
            
        return stk[-1]
            


        





            
        


        