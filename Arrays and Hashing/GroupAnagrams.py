# Approach:

# 1. Use a hm - for grouped anagrams - that is a defaultdict of type list
# 2. For each string in the list - sort the string - and use this sorted string as a key for grouping all anagrams in the list.
# 3. Finally return the values of the hashmap as a list 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # from collections import defaultdict
        # grp_anagrams_hm = defaultdict(list)

        # for s in strs:
        #     sorted_s = ''.join(sorted(s))
        #     grp_anagrams_hm[sorted_s].append(s)
        # return list(grp_anagrams_hm.values())

        # # to improve complexity
        # from collections import defaultdict
        # grp_anagrams_hm = defaultdict(list)




# This optimization is only possible - if we know for sure that it's only going to be 26 lowercase characters.
        from collections import defaultdict
        grp_anagrams_hm = defaultdict(list)

        for s in strs:
            count_char = [0]*26
            for char in s:
                # You are modifying the count of this 26 letter list - to note the freq of each lower case alphabet in the string.
                #  where 
                #count_char[0] - count of 'a's, 
                #count_char[1] - count of 'b's, etc.
                count_char[ord(char)- ord('a')] += 1
            
            key = tuple(count_char)
                
            grp_anagrams_hm[key].append(s)
        return list(grp_anagrams_hm.values())

        # this lil improvement - helps us get rid of the 'logk' element of sorting in the TC.
        # TC is now O(n*k)
        # However, SC stays the same..




# n - len(strs)
# k - max len of a str in strs

# TC - O(n*k(log(k))) - klogk for sorting each string,  for each of the strings in strs
# SC - O(n*k) -O(n) - for hashmap, and then we are storing a list for each of the keys in the hashmap.