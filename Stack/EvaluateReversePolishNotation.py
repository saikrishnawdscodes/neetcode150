#Nov 27, 23
# Approach: We use a stack to append the values as they come in.
# Append the numbers, and when an operator is arrived at, pop the last 2 values and then append the result instead
# In python using the int(a/b) - truncates the result to 0.
# be a lil careful with - and / operators - while applying them to popped vals.
# Eg., if stack has [1,2] - then the order is 1-2, not 2-1. Similarly with div as well.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c =='+':
                stack.append(stack.pop() + stack.pop())
            elif c =='-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif c =='*':
                stack.append(stack.pop() * stack.pop())
            elif c =='/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(c))
        
        return stack[-1]

# TC: O(n) - we iterrate through each ele in the tokens.. technically more like O(2n)
# SC: O(n) - we use the stack to get this done..

        