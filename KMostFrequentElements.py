# approach - bucket sort.
# 1. Use a hm to keep a freq count
# 2.Use the bucket sort algo - basically take an array called bucket_count- of size nums+1 Update the bucket_count[i+1] with the list of all numbers occuring 'i+1' times in the count_hm.count_dict
# 3. Finally reverse traverse the array - and then in the k most elements from reverse.  


# from collections import Counter
# count_hm = Counter(nums)
# print(count_hm)
# print(type(count_hm))


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_hm = {}

        for num in nums:
            if num in freq_hm:
                freq_hm[num] += 1
            else:
                freq_hm[num] = 1
        
        bucket_count = [[] for i in range(len(nums)+1)]

        for key,val in freq_hm.items():
            bucket_count[val].append(key)
        
        ans = []
        for i in range(len(nums), -1, -1):
            ans.extend(bucket_count[i])
            if len(ans) >= k:
                break
        
       
        return ans[:k]

# SC : O(n) - the hash map and list for bucket sort
# TC : O(n) - traversing through the list for counter, and then through the bucket sort array in reverse order