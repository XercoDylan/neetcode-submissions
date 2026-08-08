# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        previous = None
        slow = head

        current = 0

        while (current != n):
            fast = fast.next
            current += 1

        
        while (fast != None):
            fast = fast.next
            previous = slow
            slow = slow.next

        if  previous == None:
            return head.next
        else:
            previous.next = slow.next

        return head
