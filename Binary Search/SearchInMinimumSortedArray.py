# Approach - apply binary search - but change the conditions.

# 1. find out in which sorted array the mid is in
    # i) if nums[l] <= nums[mid] #- Left sorted array
    #     now, we need to go through left or right here.
    #     if target < nums[l] or target > nums[mid]:
    #         l = mid +1  #go left
    #     else:
    #         r = mid - 1 # go right

    # ii)  else: #- right sorted array
    #         if target < nums[mid] or target > nums[r]:
    #             r = mid - 1
    #         else:
    #             l = mid + 1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            # left sorted portion - limits - l, mid
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            else: # you're in right sorted portion - limits: mid, r
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return -1

# TC : O(n)
# SC: O(1)     