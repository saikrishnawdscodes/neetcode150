# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle pt using slow and fast ptr first
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is now at mid part 
        curr = slow.next
        prev = None

        # proceedig to reverse 2nd half of list in place
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        slow.next = None # dont forget to disconnect the first half - after reversing the second half

        # now, lets do the Merging

        l = head
        r = prev

        while r: # usually we do this till r side of LL is exhausted - cuz at times if the list size is even - the R side size is only 2, where as the L side list size includsing the mid pt is 3+1 which is 4.
            l_temp = l.next
            r_temp = r.next
            l.next = r
            r.next = l_temp
            l = l_temp
            r = r_temp
        
        

# Logic : - REVERSE AND MERGE
# ======

# task is to reorder a LL like 
# l0 -> l1 -> l2 -> l3 .... ln-1 -> ln
# to 
# l0 -> ln -> l1 -> ln-1... so on

# Use fast and slow pointers to find the middle of the list first.

# IMPORTANT POINT TO REMEMBER IS - IF YOU ARE USING FAST AND SLOW POINTERS - 
# SLOW IS GOING AT HALF OF PACE OF FAST (SLOW = SLOW.NEXT VS FAST = FAST.NEXT.NEXT) 
# SO, BY THE TIME FAST IS AT END OF LIST, SLOW IS AT MIDDLE POINT OF LIST!



# Once mid point has been identified - reverse the 2nd half of LL in place. (similar to the reverse linked list)

# DISCONNECT THE FIRST HALF AFTER THIS FOR A CLEAN MERGE! - VERY IMPORTANT

# After that, use 2 temp vars here - l_temp and r_temp - similar to the reverse LL problem - as you need to keep
# track of where you were - as you are now going to be joining 1 element of first half, and then another of 2nd half

# you dont need to return anything - just modify the LL in place thats it



