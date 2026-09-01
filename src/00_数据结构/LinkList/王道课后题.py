from typing import Optional

from util import LinkedListUtils, ListNode


# 01_删除不带头节点的单链表L中所有值为x的结点 递归
def t01_1(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    if head is None:
        return None
    head.next = t01_1(head.next, x)
    # 如果当前节点的值等于 x，跳过当前节点（相当于删除），返回后续节点；
    # 否则保留当前节点，返回自身。
    return head.next if head.val == x else head


# 01_删除不带头节点的单链表L中所有值为x的结点 非递归
def t01_2(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    if head is None:
        return

    dummy = ListNode(next=head)
    p = dummy

    while p.next is not None:
        if p.next.val != x:
            p = p.next
        else:
            p.next = p.next.next

    return dummy.next


# 04_删除带头节点单链表中的最小值(唯一)
def t04(head: Optional[ListNode]) -> Optional[ListNode]:
    if head.next is None:
        return

    min_val = 10**7  # 最小节点的值
    p = head  # 指针节点
    pre = head  # 指向最小节点的前一个节点

    while p.next is not None:
        if p.next.val < min_val:  # 更新最小节点的前驱节点和最小节点的值
            min_val = p.next.val
            pre = p
        p = p.next

    # 删除最小节点
    pre.next = pre.next.next


if __name__ == "__main__":
    raw_list = [1, 2, -3, 4, 5]
    head = LinkedListUtils.from_list_head(raw_list)
    t04(head)
    LinkedListUtils.print_list(head)
