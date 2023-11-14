# Approach - only alphanumeric chars need to be considered, 
# first convert all the alphanumeric chars to lower case, then remove the non-alpha numeric chars
# then just use 2 pointer approach - left, right - keep comparing the 2 letters encountered, till the end.


# another way to clean up the string
# import re
# cleaned_s = re.sub(r'[^A-Za-z0-9]', '', s.lower())

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
        left = 0
        right = len(cleaned_s)-1

        while left < right:
            if cleaned_s[left] == cleaned_s[right]:
                left += 1
                right -= 1
                continue
            else:
                return False
                
        return True

# TC - O(n) - traversing the string once
# SC - O(n) - creating a cleaned_s thats as long as i/p