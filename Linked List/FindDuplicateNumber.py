# 2 solution use cases exist for this problem :
    
# 1) i/p list is mutable (vals inside array can be changed) -> negative marking
# 2) i/p list is immutable (vals inside cant be changed) -> Floyd's cycle detection algorithm

# Method 2 caveats 

# only works if elements are in range 1-> N - if 0 can be one of the elements - 
# then it'll fail - cuz first element can also have incoming edges. Also, the guarantee that there is only 1 repeating element.


# Method 1 caveats - 

# Only works if all numbers are non negative. If numbers are negative - algo wont work.
# Cuz the idea itself is to see first positive element and return that as duplicate.

# We need to return the repeating element !
# Method 1 :
# ===========

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            idx = abs(nums[i]) -1 # index remapping from 1 to n - the index now becomes 0 to n-1
            if nums[idx] <0:
                return abs(nums[i])  # you need to return this number at ith index - as this has idx calc has already happened!
            else:
                nums[idx] *= -1
        return -1

# TC - O(n)
# SC - O(1)


# Logic :

# You start by remapping and creating an  idx that goes from 0 to n-1 - instead of the 1 to n that are present in the list
# idx = abs(nums[i]) -1
# Then, using the nums[idx] - you first check if its negative - if not you make it negative
# in case this if nums[idx] is already negative - then that means that the abs(nums[i]) was already present and the number was already encountered. 
# So, you return this as the duplicate element answer!


# Methhod 2 : floyd's algorithm: 
# ==============================


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True: # essentially a do-while loop needed - cuz slow and fast start off at same place- 
                    # the algo needs to run atleast once, we basically need to find out where they meet next
            
            slow = nums[slow]
            fast = nums[nums[fast]]  # this is the way to implement the fast and slow pointers. 
                                        # Write down the index to val mappping LL representation to understand this better
            if slow == fast:
                break
        
        slow2 = 0

        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow
        
# TC - O(n)
# SC - O(1)

# Logic : 

# You start by making a graph like or LL like representation of the input list.
# The nodes need to be the values of the list basically.
# Then you implement the slow and fast ptr - find where they meet - store this
# whle iterating - you assign the elements of the list to slow and fast.
# Put this in that DO..WHILE style loop - because you initialize slow and fast as 0,0 initially, and this logic needs to run atleast once to figure out the next meeting of the fast and slow.

# Then - initialize a new ptr slow2 from the start again - and then keep iterating till this slow2 and slow collide.
# This will be at the same place as the head of the list - the head of the list will basically be the value wherein multiple other nodes are connected - making it the start of a cycle!. 
# This is the duplicate element!