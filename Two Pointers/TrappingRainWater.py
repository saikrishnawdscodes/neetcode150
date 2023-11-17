# Nov 17, 23
# BRUTE FORCE
# For every index - the amount of water it can trap is 
# min(L,R) - height[i]
# L is the max height in height[:i], R is the max height in height[i+1:]
# NOTE! Be very careful about using the min and max functions in Python. Cuz if its empty list []
# min and max throw error. So, handle that properly!

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         trapped_water = 0
#         for i in range(len(height)):

#             l_list = [height[num] for num in range(i)]
#             r_list = [height[num] for num in range(i+1,len(height))]

#             if l_list and r_list:
#                 metric = min(max(l_list), max(r_list)) - height[i]
#                 if metric >0:
#                     trapped_water += metric
#             elif not l_list or not r_list:
#                 trapped_water += 0


#         return trapped_water

# TC: O(n^2) - time limit exceeded        
# SC - O(n)


# Optimized APPROACH:
# TC: O(n)
#SC - O(1)


#  The metric for this approach also remains the same - 

#  trapped_water_at_index  = min (L,R) - height [i]
 # L is the max height in height[:i], R is the max height in height[i+1:]
# But, here in this approach, we dont go through the pain of finding out the the l_list and r_list to find out
# L and R separately

# Instead, we use the 2 pointer approach - to do this. We define lp = 0, rp = len(height)-1 as always.

# The way we decide to move the lp or rp - so, if L is lower, then lp+=1
# if R is lower, rp -= 1

# Now, to find L and R as a moving changing value while we update the indices.. we initialize L to the 
# first height, and R to first height.

# So, for eg., if 
# height = [4,2,0,3,2,5], then L = 4, R = 5

# 1. We then first move the pointers - > lp + =1 / rp -= 1
# 2. Then we update the L, R accordingly as L = max(L,height[lp/rp]) - as the max ht needs to be updated..
# 3. then using the most up to date vals - we update the water contained at each index 
# L-height[i] or R - height[i] based on which ever L or R was smaller.

# THIS ORDER IS VERY IMPORTANT!!!!! UPDATE THE TRAPPED WATER ONLY AFTER MOVING THE POINTER AND UPDATING THE L,R
# 4. we finally return the o/p


class Solution:
    def trap(self, height: List[int]) -> int:
        L = height[0]
        R = height[-1]

        lp = 0
        rp = len(height)-1
        trapped_water = 0
        while lp < rp:
            if L <= R:
                lp += 1
                L = max(L,height[lp])
                water_at_index = L- height[lp]
                if water_at_index > 0:
                    trapped_water += water_at_index
                # L = max(L,height[lp])
                # lp += 1
            else:
                rp -= 1
                R = max(R, height[rp])
                water_at_index = R - height[rp]
                if water_at_index >0:
                    trapped_water += water_at_index
                # R = max(R, height[rp])
                # rp -= 1
        return trapped_water


# TC - O(n)
# SC - O(1) no extra space needed! 