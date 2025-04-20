# from typing import Optional
# class ListNode:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = None

class Solution:
    def ReverseNodesInKgroups(self,head: Optional[ListNode], k:int) -> Optional[ListNode]:
        
        def reverse_k_list_nodes(head, k):
            prev= None
            curr = head
            count = 0
            while curr and count < k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                count += 1
            return prev, head  # returning new head, new group tail
                
        
        dummy = ListNode(-1)
        dummy.next = head
        prev_group_tail = dummy
        
        while True:
            kth_node = prev_group_tail
            count = 0
            while kth_node and count < k:
                kth_node = kth_node.next
                count += 1
            
            if count == k and kth_node:
                reversed_group_head, group_tail = reverse_k_list_nodes(prev_group_tail.next, k)
                
                # connecting the new reversed group to the LL
                prev_group_tail.next = reversed_group_head
                group_tail.next = kth_node.next

                # update the pgt pointer - to continue the iteration
                prev_group_tail = group_tail
                
            else: # this gets triggered when kth node is missing - in this case no reversal or anything is needed, 
                    # furthermore - the last part of connecting a reversed group - takes care of linking the rest of the left out LL correctly
                    # so, nothing else needs to be done here!
                break

            
        return dummy.next

# TC - O(n); SC - O(1)


# Logic : We use the combo of reverse a linked list, by splitting the given linked list into segments - each of length 'k'
# The important thing is to keep track of the prev group's tail pointer and how the new reversed head and tail are returned, and then
# finally, the reversed group is merged in place into the overall i/p list.




