# Nov 18, 23
# Approach : we use the 2 pointer sliding window technique.
# We start with l = 0, r = 0
# We also maintain a set() to keep track of what characters we have encountered. While we keep coming to a character we havent encountered yet, we keep adding it to the set! 
# Once, we do encounter a duplicate, we remove the char from the set, and reset our counter of the substr, and the count of the curr length of the longest substr, and proceed.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest_substring = 0
        char_set = set()

        while r < len(s):
            if s[r] not in char_set:
                char_set.add(s[r])
                curr_substring = r - l +1
                longest_substring = max(longest_substring, curr_substring)
                r += 1
            else:
                char_set.remove(s[l]) # this is the mistake! it needs to be s[l] that is removed, not s[r]!
                l += 1
        return longest_substring

# TC - O(n)
# SC - O(n) - hashset is used