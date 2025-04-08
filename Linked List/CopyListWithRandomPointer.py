"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # pass 1 - interleave existing nodes with new nodes

        if not head:
            return None
        
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # pass 2 - link up random pointers
        curr = head
        while curr:
            if curr.random:# edge case - what if curr.random = None ? in that case we dont care about assigning the new node 
                            # anything as by defualt new_node.random = None
                curr.next.random = curr.random.next 
            curr = curr.next.next # because the interleaved nodes need to be skipped
        
        # pass 3 - separate the original and copied list

        og_head = head
        copied_head = head.next
        copied_curr = copied_head

        while og_head:
            og_head.next = og_head.next.next
            if copied_curr.next: # edge case - say if list len is only 1 - 
                                    # then copied_curr.next will become null 
                                    # if not handled properly!
                copied_curr.next = copied_curr.next.next
            og_head = og_head.next
            copied_curr = copied_curr.next
        
        return copied_head
         
# TC - O(n), SC - O(1)

# Logic - interleave existing nodes in the linkedlist with new nodes - 
# then link the random pointers to these copy nodes which have been interleaved.
# finally, separate the og and the copied lists - and return the head of the copied list.

# Keep a watch on edge cases - whereever you feel like a pointer can be null - avoid that!
        



        