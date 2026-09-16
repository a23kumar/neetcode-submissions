class Solution:
    def __init__(self):
        self.carry = 0

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        c1 = l1
        c2 = l2
        prev = None

        while c1 or c2:
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0

            tot = v1 + v2 + self.carry
            self.carry = tot // 10
            out = tot % 10

            if c1:
                c1.val = out
                prev = c1
                c1 = c1.next
            else:
                prev.next = ListNode(out)
                prev = prev.next

            if c2:
                c2 = c2.next

        if self.carry:
            prev.next = ListNode(self.carry)

        return l1
