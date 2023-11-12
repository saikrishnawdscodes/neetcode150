class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashmap = {}
        for i in nums:
            if i in hashmap:
                return True
            else:
                hashmap[i] = 1
        return False

# TC: O(n) - traverse the list one by one
# SC: O(n) - you are using a new hashmap for this.