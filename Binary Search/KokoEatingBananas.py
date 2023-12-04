# Dec 4,23
# Approach:
# Understand the problem. len(p)<=h is a given.
# Time taken to eat all piles - piles[i]/k for all piles.
# Now, we need to find min such 'k' so that 
# this total time is still < h

# k is the speed of eating. k bananas/hr.
# First, we need to determine the range of ks we need to try.

# The upper limit of k - can be fixed as max(piles) - this is because if that pile can be eaten in 1 hour, rest all other piles can be eaten in 1 h each.

# so ,k is in range [1,2,3....max(piles)]

# So, use this array and find the time taken for each 'k' - and then return the least k for which total_time > h  -- use binarysearch for this! 


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        import math
        max_p = max(piles)
        # k_list = [i for i in range(1,max_p+1)]
        l = 1
        # r = len(k_list) -1
        r = max(piles)

        min_k = r

        # total_time < h
        while l <= r:
            current_k = (l + r)//2
            total_time = 0
            for i in range(len(piles)):
                total_time += math.ceil(piles[i]/current_k)
            
            if total_time <= h:
                min_k = min(min_k, current_k)
                r = current_k - 1
            elif total_time > h:
                l = current_k + 1
        return min_k

            
# TC : O(logn*n) - O(n) - for finding total time for pile, and logn for tryin out the diff k vals.

# SC: O(1)


        