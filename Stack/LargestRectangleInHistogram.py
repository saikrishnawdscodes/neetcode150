# Dec 4, 23
# Approach: 

# We are bothered about the most recent ht we keep track of, and then we keep popping the hts. as they come. So - a STACK needs to be used.

# Stack - hold the idx, height
# keep another var max_area that'll keep getting updated.. 

# Break down all cases in the problem. Rectangles can be strictly incr, strictly decr, and a mixture in heights.
# Keep track of current rect. ht, and see if the next one is > in ht, or less than in ht. If yes, we can keep extending that ht. as a continuation

# Or else, we can just compute the area till there, and pop that ht from consideration. 
# While popping - see if the curr ht being considered is still <= the popped ht, if yes, keep the idx tracker there only - for area calc.

# THIS IS THE MOST IMPORTANT PART!!! We need to see if the index we store on top of stack can be extended back..

# Idea is after popping a ht, we see whats the next stack top element - this will help us update the max area each time.

# finally, after end of iteration - we will enp up having some elements left in stack.
# for each of these, compute theb max_Areas that we would get, before removing them from stack..


# For the code -  we just need to handle the popping case properly - cuz by default we keep appending the stack with hts if they are in asc order..


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # subarray of [idx, ht] for each element in stack
        max_area = 0

        for i,h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                popped_idx, popped_ht = stack.pop()
                max_area = max(max_area, popped_ht*(i-popped_idx))
                start = popped_idx
            stack.append([start, h])
        
        # first iteration and append and pop done till end of stack. Now, we need to see what all elemenst are left in stack.
        # this means that these elements are etending till end of stack. So, we calc their areas and update max area accordingly

        for i,h in stack:
            max_area = max(max_area, (len(heights)- i) * h)
        return max_area 


#   TC - O(n) -   we iterrate through the histogram once - and then push ele to stack once, and pop it once.

#   SC : O(n) -   we are using stack - which could go upto size of i/p array at max