# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = ListNode()
        tail = temp
           
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next = ListNode(list1.val)
                list1 = list1.next
            else:
                list2.val < list1.val
                tail.next = ListNode(list2.val)
                list2 = list2.next   
            tail = tail.next
            
        while list1 is not None:
            tail.next = ListNode(list1.val)
            list1 = list1.next
            tail = tail.next
            
        while list2 is not None:
            tail.next = ListNode(list2.val)
            list2 = list2.next
            tail = tail.next
            
        return temp.next