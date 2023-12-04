# Dec 4, 23

# Approach :
# Apply binary search twice :
# Use Binarysearch to first find out which sub list needs to be selected to search for target
# Then Binarysearch again to see if sublist contains target. 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # this func is to call the classic binarysearch on the selected sub array
        def binarysearch(nums, target):
            l = 0
            r = len(nums) -1
            while l <= r:
                mid = (l + r)//2

                if nums[mid] == target:
                    return True
                elif target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            return False


        l = 0
        r = len(matrix) - 1
        # to identify which sub array to select
        while l <= r:
            mid = (l + r) //2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                return binarysearch(matrix[mid], target)
            elif target < matrix[mid][0]:
                r = mid -1
            else:
                l = mid + 1
        return False

# TC : O (log m + log n) - for finding which sub list to consider - we run a binary search which is O(log m), and then we do another 
# binary search to see if the target ele is there is in the selected list - O(logn) , so total = O(log m + log n) = O(log(m*n))

# SC: O(1) - no extra space