# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head
        fast = head
        curr = head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
        curr = slow
        prev,nxt = None,None
        while curr!=None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        i = head
        j = prev
        while j!=None:
            if i.val!=j.val:
                return False
            i = i.next
            j = j.next
        return True