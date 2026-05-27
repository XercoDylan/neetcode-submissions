
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        current = None

        while (list1 != None or list2 != None):

            if list2 == None:
                next_node = list1
                list1 = list1.next
            elif list1 == None:
                next_node = list2
                list2 = list2.next
            elif list2.val < list1.val:
                next_node = list2
                list2 = list2.next
            else:
                next_node = list1
                list1 = list1.next

            if current is not None:
                current.next = next_node
            
            current = next_node


            if head == None:
                head = current

        return head