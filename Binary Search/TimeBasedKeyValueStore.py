# Dec 8, 23
# Approach:

# So, use a hashmap - with keys that are the given strings like bar, bar2 , etc. And the value for each key would be a list of [value, timestamp]

# GET : 

#    - this is because in the get operation - if you dont find the exact val matching the given timstamp, you need to return the TS that is closest and < the reqd timestamp. So, we have all these same values to a key  -with diff timestamps as a sublist.

# Now, in the question it is given that all the set operations are called in with TS that are increasing in order, which means that the TS in the sublist will be in sorted order already, this saves us from sorting the values in the sub list.

# So, to return the value with TS <= given TS - we can return that in O(logn) time using binary search.


# SET: 

# Set is pretty straighforward - you just need to append the existing list with a new entry in a dictionary, or add a new key val pair and add it then - this is an O(1) operation.


class TimeMap:

    def __init__(self):
        self.hm = {} # each key contains values like [[value, timestamp1], [value, timestamp2]...]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hm:
            self.hm[key].append([value, timestamp])
        else:
            self.hm[key] = []
            self.hm[key].append([value, timestamp]) 

    def get(self, key: str, timestamp: int) -> str:
        # you handle the edge case where res can be blank string, if nothing like the value is found

        res = ""
        values = self.hm.get(key, [])
        l = 0
        r = len(values) -1 
        while l <=r:
            mid = (l+r)//2

            # here, if we have TS like 1,2,3.. and say our reqd target Ts = 4  
            # - the res will be first set to 1, then overwritten as 2... etc. 
            # till finally the closest < than value to target Ts : 3 is returned 
            
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid -1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


# TC: set method - O(1); get method- O(logn)
# SC: set method & get method - O(n) 