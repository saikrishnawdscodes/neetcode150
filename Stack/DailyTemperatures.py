# Nov 29, 23
#Approach: Use a monotonically decreasing stack.. 
# Each val in stack is a pair of [index, temp]
# res = [0*len(temp)] - 0 is the def val - which would stay unchanged basically if the val is ascending only from there on..
# append vals to stack if the temps are descending.. 
# if not, then pop the last element pair - from stack, and then - for this particular idx, do res[idx] = i - idx

# do this 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = [] # pair of [idx, temp]

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                popped_idx, popped_temp = stack.pop()
                res[popped_idx] = idx - popped_idx
            stack.append([idx,temp])
        return res
            

# TC : O(n) - each element is iterated over in the loop - O(n), and then appended and popped 2 O(1)s. 
# SC: O(n) - max size of stack is n if its an strictly decreasing array