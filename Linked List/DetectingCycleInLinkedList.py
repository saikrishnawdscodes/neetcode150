# class ListNode:
#     def __init__(self,val):
#         self.val = val
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

# TC - O(n)
# SC - O(1)

# Logic : Use slow and fast pointers - to identify a loop. If at any point slow ptr is at the same place as fast ptr,
# then that means there is a loop
