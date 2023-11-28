# Nov 27, 23
# Approach - we use python lists [] for the stack here.
# We need O(1) TC for these functions... which are easy enough to implement - cuz we are using inbuilt libraries.
# The only one that needs thought is the getmin() implementation in O(1).

# To achieve this, we use another auxiliary/additional stack - called minStack - which keeps track of the min element at each level.
# For eg.,

# stack       minstack
# -----       ---------
    # -10         -10
    # -5          -5
    # 20          10
    # 15          10
    # 10          10

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self,val : int) -> None:
        self.stack.append(val)
        val = min(val,self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minStack[-1]



# TC : O(1) 
# SC - O(n) - for the extra stack for maintaining min.


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()