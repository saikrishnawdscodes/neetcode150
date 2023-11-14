# approach - its mentioned that all the numbers in array are unique, and tha only 1 unique answer exists, and that len of arr is atleast 2. So , we dont need to bother about case of edge cases too much here.

# declare a hashmap - and keep updating it with the key as the arr number, and val as the index.
# For every num - as we iterate through - we see if there is a complement that already exists in the hm
# if yes, we can stop the traversal then and there
# If not, we continue..

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, num in enumerate(nums):

            complement = target - num
            if complement in hm:
                return [i, hm[complement]]
            hm[num] = i
        

# TC: O(n) - we need to iterate through the elements in the list.
# SC: O(n) - we need a hm