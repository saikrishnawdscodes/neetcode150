# Dec 8, 23
# Approach: We are trying to come up with Optimised solution O(log(min(m,n))).
# How - We do binary search on the smaller sized array alone.
# Let smaller array be A, larger array be B (Write logic to do swapping if not)

# compute the total = len(A) + len(B)
# half = total//2 (round up)

# Compute the size of left partition of smaller array - Aleft_part_size.
# then, the left partition of larger array needs to be half - Aleft_part_size.
# Only then will the size of left partiton of merged arrays be equal to half

# EDGE-CASE_HANDLING:

# Now, say in case one of the arrays A or B is empty - or for out of bound errors..
# in that case to avoid edge case stuff set Aleft and Bleft to -infinity if ior j >=0
# Similarly, set Aleft  to +infinity if i+1  < len(A); Bleft to +infinity if j+1 < len(B)



# Idea is we know that the partition we have considered is true only if
#  Aleft < Bright and Bleft < Aright
    # IF yes, then the median is calc based on odd total or even total.
    # If odd total - median = min(Aright, Bright)
    # If even - then median =  max(Aleft, Bleft) + min(Aright, Bright) / 2

# If this is not the case - we move the l,r pointers on A indices to adjust the partition sizes.


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        if len(B) < len(A): # make the swap to ensure smaller array is always A
            A, B = B, A
        
        total = len(A) + len(B)
        half = total//2 # rouding up

        l = 0
        r = len(A) - 1
        while True:  # keeping l<=r wont work here.. you need to keep while True
            i = (l+r)//2 # i is mid index of A
            j = half - i - 2  # j is mid index of B

            Aleft = A[i] if i >=0 else float('-infinity')
            Bleft = B[j] if j >=0 else float('-infinity')
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity") 

            if Aleft <= Bright and Bleft <= Aright:
                # we have now found correct left partition for the merged array
                if total %2: # if total is odd
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
            #if left partition size is not right / is not validated
            elif Aleft > Bright:
                r = i-1
            else:
                l = i+1

# TC : O(log(min(m,n)))
# SC : O(1)



        
       

