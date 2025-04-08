class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class Solution:
    def Add2numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry: # adding carry - edge case here! dont forget! because till last carry over digit new node needs to be added
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum = v1 + v2 + carry
            carry = sum//10
            val = sum % 10
            new_node = ListNode(val)
            curr.next = new_node

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
    
            
# TC - O(m+n) - where m, n are sizes of the input lists
# SC - O(1) extra space.

# Logic : 

# The reversed numbering helps in iterating the sum of numbers along with sending carry over to next node.
# We iterate through the l1 and l2 till they are there - if they arent there - we make the other one 0.
# Finally, we do this till the last carry is also added! That's the edge case - we need to account for! 
# as we iterate through nodes - we add them and then add the units place of the sum - and the carry is taken forward.