# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head and not head.next and n == 1:
            return head.next

        curr = head
        l = 0
        while curr:
            l += 1
            curr = curr.next

        if n == l:
            return head.next

        steps = l - n - 1
        curr = head
        p = 0
        while p < steps:
            curr = curr.next
            p += 1

        if curr.next:
            curr.next = curr.next.next

        return head



        
