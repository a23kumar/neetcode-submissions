# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return                         # nothing to do

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 2. reverse second half
        second = slow.next                # start of 2nd half
        slow.next = None                  # detach 1st half
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev                     # 'prev' is new head of reversed half

        # 3. merge halves alternately
        first = head
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next
