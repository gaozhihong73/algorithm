# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution1:
    """沿用src/08_链表/24_两两交换链表中的节点.py的逻辑，会报空间溢出，因为空间复杂度到了O(n)，超出题意规定"""

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        h = ListNode()
        tail = h
        p = head

        nodes: ListNode = []
        while p != None:
            nodes.append(p)
            p = p.next
            if len(nodes) == k:  # 倒序使用尾插法，最后清空 nodes 数组
                for i in range(k - 1, -1, -1):
                    tail.next = nodes[i]
                    tail = nodes[i]
                nodes: ListNode = []

        if len(nodes) != 0:  # 若列表中还剩余节点，那么久顺序使用尾插法
            for i in range(len(nodes)):
                tail.next = nodes[i]
                tail = nodes[i]
            tail.next = None
        return h.next


class Solution2:
    """
    四指针 计数法
    """

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:  # 处理特殊情况
            return head

        h = ListNode()  # 新链表的表头

        pre = h  # 始终指向下一组的开头，或者说是当前组的末尾
        p = head  # 指向当前元素的遍历指针
        pn = p  # 总是指向下一组的开头
        pre_n = None  # 记录当前组的第一个元素（翻转之后就变成了当前组的最后一个元素了），以供 pre 跳转使用
        count = 0  # 记录pn遍历过的个数
        while True:
            while pn is not None and count != k:
                """
                pn 向后遍历，遍历到下一个住的开头，或者遍历到链表结束就停止
                """
                if (
                    count == 0
                ):  # 记录当前组第一个节点，这个节点在翻转后将会是该组最后一个节点
                    pre_n = pn
                count += 1
                pn = pn.next

            if count == k:  # 如果收集满一组了，开始翻转
                while p != pn:
                    """
                    以 pre 节点为头节点，使用头插法
                    """
                    temp = p
                    p = p.next
                    temp.next = pre.next
                    pre.next = temp
                pre = (
                    pre_n  # 翻转结束后，pre 跳到该组的结尾，可以看作是下一个组的头节点
                )
                count = 0  # 计数器归零

            if pn is None:  # 链表遍历完毕，跳出循环
                break

        if count > 0:  # 如果最后一组不足k个节点，不翻转，使用尾插法
            pre.next = pre_n

        return h.next


class Solution:
    """
    计算分组法
    """

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:  # 处理特殊情况
            return head
        n = 0
        p = head
        while p is not None:
            n += 1
            p = p.next

        n //= k  # 最多能分为完整的 n 组

        p = head
        h = ListNode()  # 新链表的表头
        tail = h
        head_tail = None

        for _ in range(n):
            for j in range(k):
                if j == 0:
                    head_tail = p

                temp = p
                p = p.next
                temp.next = tail.next
                tail.next = temp
            tail = head_tail

        if p is not None:
            tail.next = p

        return h.next


if __name__ == "__main__":
    e = ListNode(5, None)
    d = ListNode(4, e)
    c = ListNode(3, d)
    b = ListNode(2, c)
    a = ListNode(1, b)

    Solution().reverseKGroup(a, 3)
