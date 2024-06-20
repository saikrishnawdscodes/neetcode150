# this question is an easy one - we just need to keep 2 cases in mind
# C1: if the 2 lists are empty - we need to return an empty list - so keep a dummy node alive
# C2 : if l1 or l2 is larger - then automatically, when one gets over - just link the rest of the other list which remians.

# TC - O(n); SC - O(1) ignore the list created for the o/p

class Solution:
    def mergeTwoLists(self, l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        head = dummy_node

        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1:
            head.next = l1
        else:
            head.next = l2
        return dummy_node.next