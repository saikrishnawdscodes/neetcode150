# Nov 27, 23

# Approach : Use a list as a stack. use the append and pop operations, 
# use a hashmap with the diff kinds of open, closed brackets as pairs.

# iterate through the string.. we basically append only the open brackets to stack.
# if the last added bracket to stack's value in hashmap and the current bracket are not same - return false. - here order is messed up cases.
# also here we need to make sure that stack is not empty.. if stack is empty - then likely that a closed barcket of some kind has been added- before it's opening bracket.

# after the iteration is done - if the length of stack is empty - then valid 
# cuz all the corresponding closed brackets have occured in the right order and we've popped all of the appended, opening brackets from the stack


class Solution:
    def isValid(self, s: str) -> bool:

        hm = {"(":")", "{":"}", "[":"]"}
        stack = []

        for bracket in s:
            if bracket in hm:
                stack.append(bracket)
            
            elif not stack or bracket != hm[stack.pop()]:
                return False
        
        return len(stack) ==0

# TC - O(n)
# SC: O(n) - extra space for hm, stack

