# Approach - use 2 pointers - one left, one right
# Make use of the fact that the array is sorted, so we dont need any additional space 
# if the sum>target -  obv then we need to decrease the sum of the 2 nos. being considered. 
# So reduce the sum by decreasing the larger number from being included in the summ - ie.,  right -1
# and vice versa - left + 1 

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        
        if len(numbers) ==2:
            return [1,2]

        while left<right:
            sum = numbers[left] + numbers[right]
            if  sum == target:
                return [left+1,right+1]
                break
            else:       
                if sum > target:
                    right -= 1
                else:
                    left += 1

#TC - O(n) - we traverse through the list of numbers
# SC - O(1) - we dont use any extra space.