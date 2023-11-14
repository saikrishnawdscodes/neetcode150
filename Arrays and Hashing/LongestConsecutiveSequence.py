# Approach:
# Visualize - consider all of the numbers are on a number line..
# How would you know that something is the start of a sequence - by knowing that there is no left element.

# 1,2,3,4      100   200

# So, seeing here : 1 is the start of a seq - as there is no 0 in the list.
# Similarly, 100, 200 are also start of a seq, but 2,3,4 are not - as they all have their prev numbers in the seq.
# current_seq_len = 1
# For every start of seq - increase the len of current_seq_len

# Use a hash set for quickly checking to see if an element is there in the set.
 # maintain a longest_consec_seq = 1, and keep doing like 
# longest_consec_seq = max(curent_seq_len,longest_consec_seq)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_consecutive_sequence = 1

        if not nums:
            return 0

        for num in nums_set:
            if num-1 not in nums_set:
                current_seq_len = 1
                while num+1 in nums_set:
                    current_seq_len += 1
                    num += 1
                longest_consecutive_sequence = max(longest_consecutive_sequence, current_seq_len)

        return longest_consecutive_sequence

# SC - O(n) - we need an extra hash set for the list of nums
# TC - O(n) - we traverse through the set once..