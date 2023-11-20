
# Nov 20, 23
# Approach - use the same sliding window.
# instead of using the hashmap for keeping count of chars for each subwindow - which is costlier,
# we use the same freqcounter using array.
# So, if string is 'abc', the the count_s1 would be a 26 char long list, where count_s1[0] = 1, count_s1[1] = 1, etc.. (each index represents count
# of each alphabet)

# we use the sliding window - window size = len(s1) at a time. If at any point count_s1 == count_s2, then I return True - permutation ofsubstring found!


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1 = [0]*26
        count_s2 = [0] *26

        # First, initializing the count_s1 and count_s2 for the 1st iteration:

        for i in range(len(s1)):
            count_s1[ord(s1[i])- ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1

        if count_s1 == count_s2:
            return True

        for i in range(len(s1), len(s2)):
            count_s2[ord(s2[i]) - ord('a')] += 1
            count_s2[ord(s2[i-len(s1)]) - ord('a')] -= 1

            if count_s1 == count_s2:
                return True
        return False

# TC : O(len_s1+ len_s2) it's O(26*n) approx - cuz we run the if count_s1 == count_s2 for each window.. 
# S : O(26) - ~= O(1) as 26 letter constant list is used throughout..

# OPTIMIZATION:

# We can get rid of this O(26*n) to O(n) - by removing the if count_s1 == count_s2 part.
# Use a variable called matches.. this matches will have a max val of 26 - if the counts of all alphabets in both s1 and s2 match.. when this matches variable rwaches 26 by the end of last window - then retun true, else false
        