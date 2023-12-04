# Dec 4, 23
# Approach: Same binary search - but the coinditions for binary search need to be changed
# During start of every iteration - update the global min_val with the current mid val

# case1:  if len(arr) = 1 or  if array is already sorted/ you are left with
# a sorted subarray

# case2: when array is in rotated form and length is >1
# Here, see if the mid val > starting val - if yes - just consider the right half.(as you want min)
# else - consider left half


# finally, return the min_val

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        min_val = nums[0]

        while l <= r:
            #first consider the case of when the list is already in sorted fashion, or n rotations have been done - where n is len of array.
            if nums[l] < nums[r]:
                return min(min_val, nums[l])
            # all these if some rotations have been done
            mid = (l+r)//2
            min_val = min(min_val, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return min_val


# TC : O(logn)
# SC : O(1)      
        


        