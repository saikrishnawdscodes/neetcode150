# BRUTE FORCE
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         cords = []
#         for i,h in enumerate(height):
#             cords.append([i+1,h])

#         # print(cords)

#         max_water = 0
#         for i in range(len(cords)):
#             for j in range(i+1,len(cords)):
#                 local_max_water = min(cords[i][1], cords[j][1]) * abs(cords[i][0]-cords[j][0])
#                 max_water = max(max_water, local_max_water)

#         return max_water

# Nov 17, 23

#Approach: Use the 2 pointer approach.
# 1. Key thing is how do we update the right and left ptr.
# 2. This sum naturally prefers the l,r ptr apprach - as width needs to be maximum. So, l, r need to be 
# as spread apart as possible.

# 3. Now, comes the update part - we check which ever ht is less - whether at index l or index r, and we move that pointer. Cuz for max water capacity, obv the ht of container needs to be more..
# 4. In the case where the hts are equal, doesnt matter which ever l or r we decide to move - cuz on one side the height of the container is fixed...

# 5. After each iter, we update a max_water = max(max_water,local_area) = and finally return the o/p


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_water = 0
        while l <r:
            width = r-l
            height_of_container = min(height[l], height[r])
            local_area = width * height_of_container
            max_water = max(max_water, local_area)

            if(height[l] <= height[r]):
                l += 1
            else:
                r -= 1
        return max_water

#TC - O(n)
# SC - O(1)