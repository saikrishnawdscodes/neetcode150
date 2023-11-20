# Nov 19, 23
# Approach : Use 2 pointer sliding approach
# l = 0, r = 0, keep updating r till r < len(string) update a hashmap with the freq of the next letter.
# longest_substr = 0
# Now, the most important thing here is - how to find if a window is valid,
# ie., is the window size good enough for < k replacements - for getting a long substring. thewn update the longest_substr with longest_substr = max(window_size, longest_substr)
# if window is not valid, update the count in the hash map - and then increment the l += 1 - basically shorten the window till the longest substring with <=k replacements is founf



# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:

#         l = 0
#         r = 0
#         max_len = 0
#         freq_hm = {}
#         while r < len(s):
#             freq_hm[s[r]] = freq_hm.get(s[r], 0) + 1
            
#             window_len = r -l +1
#             if window_len - max(freq_hm.values()) <= k:
#                 max_len = max(max_len, window_len)
                
#             else:
#                 if freq_hm[s[l]] > 1:
#                     freq_hm[s[l]] -= 1
#                 else:
#                     del freq_hm[s[l]]
                
#                 l += 1
#             r += 1
#         return max_len

# TC : O(26.n) ~= O(n) - cuz for every iteration - we check a hash map with constant size of 26 - as only 26 upper case letters exist here in this question in the string
# SC - O(26) ~= O(1) as we are maintaining a hashmap that can be at most 26 chars long!

# # OPTIMIZATION!!!!! O(26*n) to O(n):
# ======================================



# Keep a max_frquency 'max_f' that can reflect the maxfreq_hm.values().. wihtout doing this operation which is what brings in the O(26) factor

# max_f = 0 // initially
# and then 
# while r < len(s):
#         freq_hm[s[r]] = freq_hm.get(s[r], 0) + 1
#         max_f = max(max_f, freq_hm[s[r]]) # this is added!

# # and then in the if statement, make the replacement 
#         if window_len - max_f <= k:

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        r = 0
        max_len = 0
        max_f = 0
        freq_hm = {}
        while r < len(s):
            freq_hm[s[r]] = freq_hm.get(s[r], 0) + 1
            max_f = max(max_f, freq_hm[s[r]]) # added
            
            window_len = r -l +1
            # if window_len - max(freq_hm.values()) <= k:
            if window_len - max_f <= k:
                max_len = max(max_len, window_len)
                
            else:
                if freq_hm[s[l]] > 1:
                    freq_hm[s[l]] -= 1
                else:
                    del freq_hm[s[l]]
                
                l += 1
            r += 1
        return max_len

# Earlier Runtime - 115ms (Beat 46.25 % users) 

# Now, Runtime - 92ms (Beat 75.28% users)
# This is a significant improvement - at large scale.

# New TC : Strictly O(n)
# SC : same as old - O(26 ~= O(1))