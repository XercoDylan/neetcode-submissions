# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        current = None

        while (list1 != None or list2 != None):
            if new_head == None:
                new_head = ListNode()
                current = new_head
            if list2 == None or (list1 != None and list1.val < list2.val):
                current.val = list1.val
                list1 = list1.next
            else:
                current.val = list2.val
                list2 = list2.next

            if (list1 != None or list2 != None):
                new_node = ListNode()
                current.next = new_node
                current = new_node

            



        return new_head
            
        