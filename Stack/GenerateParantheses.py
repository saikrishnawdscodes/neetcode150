# Nov 28, 23
# Approach:
# Use backtracking - for this problem.
# Backtracking in general is used when ever we see cues like all possible combinations,etc.
# We build the state space tree - by expanding from root node - by DFS and identify the right solutions according to the bounding conditions.

# The backtrack - is implemented by doing the stack.pop() - where we undo the operation and do the other possible combo.

# Base case - when openN = closedN = n
    # return the res
# Recursive cases - when openN < n and when closedN < openN
    # continue the recursion with updated openN & closedN values.

# begin by calling backtrack(0,0) - which stand for  0 openN and o closedN
# We append both the closed and open brackets to the stack.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            #base condition
            if openN == closedN == n:
                res.append("".join(stack))
                return res
            # recursive conditions
            if openN < n:
                stack.append("(")
                backtrack(openN +1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0,0)
        return res

# TC : O(2^(2n)) ~= O(2^n) - as at each recursion level - 2 possible outcomes at each level, and there are 2n levels
# SC : O(2n) - For recursive backtracking, what matters is the call stack space 
# The max size of the stack is going to be 2n - as there are gonna be n closed and n open brackets in the stack maximum.