# Approach - 

# 1. use just one array - called 'result'
# 2. first calculate the left prod - on top of the redsult array.
# 3. then calc the right prod, and replace the value directly in the left_product array directly! 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)

        left_prod = 1

        for i in range(1, len(nums)):
            left_prod *= nums[i-1]
            result[i] = left_prod

        right_prod = 1
        for j in range(len(nums)-2,-1,-1):
            right_prod *= nums[j+1]
            result[j] *= right_prod

        return result


# TC: O(n) - as we are itertaing through the array only once
# SC - O(1) - considering that result array is not counted as extra space..