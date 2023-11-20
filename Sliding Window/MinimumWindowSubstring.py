# Nov 20, 23

# Approach:

# We use the 2 pointer sliding window. l = 0 , r= 0 and slide r and l
# Set global res and res_size for the min substring and its size. 
# initialize res_size = math.inf and decrease it as we go.
# 2 hms - count_t, window for freq count of string t and the current window in the string s

# 2 vars - need and have - that reflect the number of character matches we have in string t, and what we currently need from the 
# window in s.

# first we update the window dict with s[r] - and the count - as we move through.
# we then check if the count of that var in the window and t is same - if yes then we increment have.


# Then comes the part where we find the min window.. we try reducing the window size - by reducing size from left.
# Check If the new reduced window still satisfies the cond - by have == need.

# first check - if the new window size is less than the current res_size - if yes update.

# Then we update the counts of the vars in the window accodingly and move the l ptr

# we then update the have var - if the new window doesnt satisfy the count conds. by have -= 1

# FOR EACH CHECK WRT count_t - use the if s[r] in count_t or if s[l] in count_t - for avoiding KEY ERRORS!
# Finally return the res substring!


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import math
        if t == "":
            return ""

        count_t, window = {}, {}

        for letter in t:
            count_t[letter] = 1 + count_t.get(letter, 0)

        need = len(count_t)
        have = 0

        res = [-1, -1]
        res_size = math.inf
        l = 0
        r = 0

        while r < len(s):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in count_t and window[s[r]] == count_t[s[r]]:  # add the s[r] in count_t check - because if thats not there, it will throw key error
                have += 1

            while have == need:
                if (r - l + 1) < res_size:
                    res = [l, r]
                    res_size = (r - l + 1)

                window[s[l]] -= 1 # add this here regardless, because we need to decrement the count of the l ptr in the window dict, before moving it
                
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:   # we need to decrement have only if we have less of the count of vars than in the count_t. Say if we have excess
                                                                # of 1 var. Eg., If we need 3 As but already have 4 As then no need to do have -= 1- because removing 1 A will still
                                                                # let us match the As in count_t
                    have -= 1
                l += 1

            r += 1  # Move the r pointer in the while loop
        if res_size != math.inf:
            return s[res[0]: res[1] + 1]
        else:
            return ""


# TC : O(s + t), where 's' is the length of string 's' and 't' is the length of string 't'.
# SC : O(s + t) due to the dictionaries 'count_t' and 'window'.