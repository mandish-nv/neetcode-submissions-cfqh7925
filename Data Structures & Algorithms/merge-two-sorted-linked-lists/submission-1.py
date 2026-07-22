# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        temp = list3

        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                temp = temp.next
                temp.val = list1.val
                list1 = list1.next
            elif list1.val >= list2.val:
                temp.next = list2
                temp = temp.next
                temp.val = list2.val
                list2 = list2.next

        if list1:
            temp.next = list1
        elif list2:
            temp.next = list2

        return list3.next
