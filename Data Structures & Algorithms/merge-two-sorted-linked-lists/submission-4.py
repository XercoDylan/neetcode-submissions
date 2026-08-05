# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        current = None


        while (list1 != None and list2 != None):
            value = None

            if list1.val < list2.val:
                value = list1.val
                list1 = list1.next
            else:
                value = list2.val
                list2 = list2.next
            
            if current == None:
                current = ListNode(value)
                newHead = current
            else:
                newNode = ListNode(value)
                current.next = newNode
                current = newNode

        if list1 != None or list2 != None:
            

            if current == None:
                current = list1 or list2
                newHead = current
            else:
                current.next =  list1 or list2



        return newHead