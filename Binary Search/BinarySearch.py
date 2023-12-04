# Dec 4, 23
# Approach : Classic binary search implementation.
# we can use the recursive or iterative approach. 

# always make sure mid is >= 0 - thats why set mid  = (l+r)//2 - rather than mid = (l + r-1)//2
# Be careful with edge case where len(nums) =1... 

# For eg., nums = [5], target = 5 /// here expected o/p is 0
# If mid = (l + r-1)//2 In this case the mid becomes -1 which gets returned. whereas the correct ans is 0 which is the index of 5 
# which is indeed present in nums

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l + r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid -1
            
            else:
                l = mid+ 1
        
        return -1

# TC : O(logn)
# SC : O(1)