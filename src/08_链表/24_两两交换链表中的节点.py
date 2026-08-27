# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    """
    节点两两一组，存入nodes数组中，再倒序使用尾插法插入新链表中
    若最后还剩一个节点，直接尾插在最后面即可
    """

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        h = ListNode()
        tail = h
        p = head

        nodes: ListNode = []
        while p != None:
            nodes.append(p)
            p = p.next
            if len(nodes) == 2:  # 倒序使用尾插法，最后清空 nodes 数组
                nodes[1].next = nodes[0]
                nodes[0].next = None
                tail.next = nodes[0]
                tail = nodes[1]
                nodes: ListNode = []

        if len(nodes) == 1:  # 若链表中节点的个数为奇数个，处理最后剩余的一个
            tail.next = nodes[0]
            tail = nodes[0]
            tail.next = None

        return h.next


class Solution:
    """
    通过 pre、p、pn 三个节点轮番遍历实现
    p 指向当前节点
    pn 指向当前节点的下一个节点
    pre 指向当前节点的前一个节点
    目的是为了让 p 和 pn 所指向的节点互换，然后pre指向互换后的节点
    具体实现为：
        p.next = pn.next   p 直接指向 pn 的下一个节点
        pn.next = p     pn指向p
        pre.next = pn    pre 指向 pn, 此时 pn 是指向 p 的，p 又指向 原来pn后面的节点，表现为 pre → pn → p → ……
    已经实现我们的需求，接下来只需要让循环跑起来就行
        pre = p (指向当前两个节点组的最后面，准备链接下一组)
        p = p.next （可能为空）
        若p目前不为空，pn = p.next
    """

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        h = ListNode()

        pre = h
        p = head
        pn = p.next

        while p != None and pn != None:
            p.next = pn.next
            pn.next = p
            pre.next = pn

            pre = p
            p = p.next

            if p != None:
                pn = p.next

        return h.next
