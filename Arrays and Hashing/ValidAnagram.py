# approach - construct 2 hash maps - for each string,
# first see if the len of 2 strings is same - if not straight away return False
# then compare if the 2 dicts are equal by simply s_dict == t_dict that's it  

# Unicode character case :
# for char in s:
#     t_dict[char] = t_dict.get(char,0) + 1     

#     t_dict[ord(char)] = t_dict.get(ord(char),0) + 1   ==> do this instead


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_dict = {}
        s_dict = {}

        if (len(s)!=len(t)):
            return False

        for char in t:
            t_dict[ord(char)] = t_dict.get(ord(char),0) + 1
        
        for char in s:
            s_dict[ord(char)] = s_dict.get(ord(char),0) + 1
        
        if t_dict == s_dict:
            return True
        return False
        

# TC: O(S+T) - S is len(s), T is len(T) - which is O(n) esstentially. 
# SC :O(S+T) - we need O(n) storage - 2 extra hashmaps.