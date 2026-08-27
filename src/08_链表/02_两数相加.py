# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l3 = ListNode()
        tail = l3
        carry = 0

        while l1 != None or l2 != None:
            a = 0 if l1 == None else l1.val
            b = 0 if l2 == None else l2.val
            s = a + b + carry
            node = ListNode(val=s % 10)
            tail.next = node
            tail = node

            carry = s // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry != 0:
            tail.next = ListNode(val=carry)

        return l3.next
