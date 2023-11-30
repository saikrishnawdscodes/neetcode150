# Nov 30, 23
# Approach - use a sorted pair of position and speed, and iterate on it in the reverse order.
# USe a stack to keep track of count of car fleets at end. basically len of stack at end is our result.

# logic is - we calc the time it takes each car to reach destination. T = D/S = target - position/ speed
# we append this time to our stack

# if len of stack is just 1 - then just one car - we dont need to bother checking for car fleets.
# so, idea is while iterating from back.. means 

# car->                                           car1    car2    car3
# position - >                                     1        5       10     12=target
# speed    ->                                      2        7        1
# time to reach target = target - position/speed   5.5      1        2

# So here, time for car2 < car 3 - so these 2 form a car fleet.

# so car 3 would be stack[-2] and car 2 would be stack [-1]
# if stack[-1] <=stack[-2]: # car 2 is faster than car 3 - collision
#     stack.pop() # keep track of just one fleet - as car 1,2 are now 1 entity in the stack

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [[p,s] for p,s in zip(position, speed)]

        for p,s in sorted(pairs)[::-1]: # reverse traversal of sorted pairs
               # makes [[10, 2], [8, 4], [0, 1], [5, 1], [3, 3]]  to [[0, 1], [3, 3], [5, 1], [8, 4], [10, 2]]
            stack.append((target - p)/s)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

# TC - O(nlogn) we sort the pairs - that is dominant to traversing through the lists.
# SC - O(n) - we use stack that will be size N at worst - if all cars form 1 fleet, pairs[] also O(n)