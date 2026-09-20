# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, head1: ListNode | None, head2: ListNode | None) -> ListNode | None:
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        if head1.val<head2.val:
            head1.next = self.mergeTwoLists(head1.next,head2)
            return head1
        else:
            head2.next = self.mergeTwoLists(head1,head2.next)
            return head2

