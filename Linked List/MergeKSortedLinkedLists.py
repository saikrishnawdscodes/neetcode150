# Brute force Logic:
# Iterate through all the k lists inside - and populate each ofthe n node vals into a list - sort that list -and then create new nodes and link these sorted vals into new nodes


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sort_list = []
        
        for list in lists:
            while list:
                sort_list.append(list.val)
                list = list.next
        sort_list = sorted(sort_list)
        print(sort_list)

        dummy = ListNode()
        tail = dummy

        for ele in sort_list:
            new_node = ListNode(ele)
            tail.next = new_node
            tail = tail.next
        return dummy.next
        


# TC : O(nlogn) - where n is total no. of nodes.
# SC : O(n)




# Optimal Divide and Conquer iterative Logic - based on merge sort logic: 
# We extend the problem of merging 2 sorted linked lists - to solve this problem
# We use merge sort technique - sort 2 lists at a time and then sort the reduced number of lists to be sorted by a factor of 2 each time.
# so, step 1 - we have k lists
#  step 2 - we have k/2 lists
# step 3 - we have k/4 lists .... this would happen logk base 2 - basically logk times

# Lets say n is the number of elements across all lists - so we process each element logk times
# so, overall TC = O(nlogk)
# For space complexity - it is O(k) - according to merge sort we create a new list each time we do the merge operation to store the 2 sorted lists at a time. 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 0:  # to get rid of edge cases
            return None
        
        while (len(lists)>1):
            merged_list = []
            for i in range(0, len(lists), 2): # this is imp - we iterate over 2 lists - and merge them
                list1 = lists[i]
                list2 = lists[i+1] if (i+1) < len(lists) else None                                 # i+1 can easily go out of bounds - be careful

                merged_list.append(self.MergeTwoSortedLists(list1, list2))
            lists = merged_list
        return lists[0]

    def MergeTwoSortedLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next


# TC : O(nlogk) - where n is total no. of nodes; k is the no. of inside lists.
# SC : O(k)


# COMPARISION : The divide & conquer logic is better - see..

# k - the number of lists will always be >= the no. of nodes 'n'
# So, the O(nlogk) is better than O(nlogn) - where in n is the no. of total nodes - the brute force doesnt even care how many k lists are there.
# So, obv the O(k) SC is better than O(n)
# the only case where these 2 approaches will be equally optimal is if each of the k lists have just node. 
# When each of the k lists contains just 1 element, the total number of elements n is equal to k. In this specific scenario:

# Brute Force TC: O(k log k)
# Divide and Conquer TC: O(k log k)