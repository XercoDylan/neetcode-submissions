# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head :Optional[ListNode]) -> None:
        previous = None
        current = head

        while (current != None):
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous

    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head


        while (fast.next != None and fast.next.next != None):
            fast = fast.next.next
            slow = slow.next

        first_part = head
        second_part = self.reverseList(slow)
        slow.next = None

        while (first_part != None):
            next1 = first_part.next
            next2 = second_part.next

            first_part.next = second_part
            second_part.next = next1

            second_part = next2
            first_part = next1






        