# Nov 17, 23

# Approach :
# 1. for 3Sum - iterate through each element 'num', and for each element, find a pair such that target sum of the pair = '-num'.
#     Adding all the 3 nums would give us num + (-num) = 0! 
# Use this as an extension of the TwoSumII problem.

# 2. So, sort the i/p arr first.
# 3. declare the res = []
# 3. If the first ele itself in the sorted arr is  >= 0 - then there is no soln possible, so just return the blank arr.append
# 4. Else, if i==0, or nums[i-1] != nums[i]   then call the TwoSumII method
#     The nums[i-1] != nums[i]
#     The purpose of this condition is to skip duplicate elements in the outer loop. 
#     (if the same number is coming again - then the same target of -num will come up. question says duplicates shouldnt be there)
#     If the current element is the same as the previous one, we skip the current iteration to avoid duplicate triplets

# 5. The params passed to the TwosumII are the res, i(the current ele from which we are checking in outer loop), orig nums arr.arr

# 6. Do the same check - target = nums[i] + nums[lo] + nums[hi]. We assign lo = i+1, hi = len(nums)-1
# 7. Do the usual Twosum checks.. but in last condn., we need to add some statements after we append a successful entry in the res

# while lo <hi:
#     if nums[lo-1] == nums[lo]:
#         lo += 1

# This is done to avoid duplicate triplets. Here in the same outer loop pass -  say arr = [-40,-30,-20....., 10, 20, 20, 20, 20]
# currently nums[i] = -40

# So, we first encounter.. stuff like lo, hi right.. so 10,20, then 20, 20.. - which will become a result - we'll append it like res.append([-40, 20, 20])
# This if condn check makes sure taht the same 20, 20 doesnt get added to the triplicate list again.




class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i ==0 or nums[i-1] != nums[i]:
                self.TwoSumII(nums, i, res)

        return res

    def TwoSumII(self, nums,i,res):
        lo = i+1
        hi = len(nums)-1
        while lo < hi:
            target = nums[i] + nums[lo] + nums[hi]
            if target > 0:
                hi -= 1
            elif target < 0:
                lo += 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo-1] == nums[lo]:
                    lo += 1
        

# TC: O(n^2) - as there is one for loop in the first function - and then again another sub loop in the TwosumII function
# SC: O(1) - no extra space as such is used. Inplace sorting only done, and we are running checks on it.


# mistakes you made first time:
# ===============================

# 1. using  
# while lo < hi :
#         if nums[lo-1] == nums[lo]:
#             lo += 1

#             instead of 

# while lo < hi and nums[lo-1] == nums[lo]:
#                     lo += 1

# this just evaluates many more conditions if duplicates are present - leading to time out issue.

# 2. break condition forgotten, and just put return res directly there..
# 3. put target = nums[i] + nums[lo] + nums[hi] outside the while lo < hi check, instead of inside