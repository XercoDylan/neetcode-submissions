# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        length = 0

        while (head != None):
            length += 1
            head = head.next

    
        return length
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.getLength(head)

        if length == 1:
            return None

        remaining = (length - n)
        curren_head = head

        if remaining == 0:
            return head.next

        while (remaining > 1):
            curren_head = curren_head.next
            remaining -= 1

        curren_head.next = curren_head.next.next

        return head

        



        