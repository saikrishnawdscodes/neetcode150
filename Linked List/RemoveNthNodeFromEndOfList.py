# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        left = dummy
        dummy.next = head
        right = head
        count = 0
        while count <n:
            right = right.next
            count += 1
        
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next

        return dummy.next # if you give return head - this is wrong. Take the case where head = [1] , n = 1. 
                            # result should be [], but here we would still return [1] as head still points to the 1 node. 
                            # Thats the reason why using the dummy  and dummy.next saves us a lot of troubles with edge cases!

# TC - O(n), SC - O(1) - single pass we get the job done!

# Logic:

# USe 2 pointers! 
# Use a left, right pointer. left pointer points to dummy, right is dummy.next which is head! 
# first iterate only right ptr n times; after this iterate the left and right till right is not none!

# Now, the left pointer is just to the left of the node to be removed! so basically remove left.next by doing
# left.next = left.next.next

# finally, return dummy.next and not head! (reason stated above in code comment)

# DONE!

       
        

        

        