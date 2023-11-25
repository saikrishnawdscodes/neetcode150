
# Nov 25,23
# Sliding Window Maximum:

# Approach: Monotonically decreasing queue.
# Sliding window - along with maintaining a deque for O(1) insertion and deletion.
# Use the indices as the queue elements... (this will help if the nums have many duplicate elements.)

# 5 incoming ...
#     8,4,3,2 - > curr queue.. NON EMPTY QUEUE..
#     keep popping till the last ele in queue is <> the nums[r] - we only need the max ele.. so its ok if we discard this.
#     Then append the curr element.

# each window - shifts to the right by 1..
# so we need to pop the queue from the left till the l and q[0] match up.

# If left pointer index 'l' > q[0] - >
# we keep popping from left.. till the q[0] index catches up with l.

# Finally comes the part where you append the o/p array - at the end of each o/p
# handle the edge case - append the p/p array only if the window is atleast size k, not before that ! 

# so, if r+1 is >=k - only then we add the q[0] - which is the max ele in queue at any point in time to the o/p arr.
# Then we increment the left pointer.. and the right ptr.

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque() # monotonically decreasing queue - of nums indices

        l = 0
        r = 0
        output = []

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if r+1 >= k: # kind of an edge case - append the output only when atleast 1 window size is reached by the r ptr 
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
                

# TC : O(n) - we eliminate the O(k) for each ele by using the queue - with O(1) for deletion and insertion
# SC : O(n) - extra queue used.