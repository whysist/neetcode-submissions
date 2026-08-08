class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans=0
        stack=[]
        for token in tokens:
            if token in "+-*/":
                val2=stack.pop()
                val1=stack.pop()
                val=0
                match token:
                    case "+": val=val1+val2
                    case "-": val=val1-val2
                    case "*": val=val1*val2
                    case "/": val=int(val1/val2)
                stack.append(val)
            else:
                stack.append(int(token))
            # print(token,stack)
        return stack[-1]
            
        