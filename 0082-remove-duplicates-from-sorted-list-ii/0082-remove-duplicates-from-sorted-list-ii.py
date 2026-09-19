# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        curr = head
        prev = None
        while curr!=None:
            if curr.next!=None and curr.val == curr.next.val:
                data = curr.val
                while(curr!=None and curr.val == data ):
                    curr = curr.next
                if prev==None:
                    head = curr
                else:
                    prev.next = curr
                
            else:
                prev = curr
                curr = curr.next
        return head