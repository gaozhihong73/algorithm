from typing import Optional

from linklist_util import LinkedListUtils, ListNode


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
def t04(head: Optional[ListNode]):
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
    min_node = pre.next
    pre.next = pre.next.next
    del min_node


# 05_将带头节点的单链表就地逆置（空间复杂度为O(1)）
def t05(head: Optional[ListNode]) -> None:
    """原地逆置带头结点的单链表（头插法）。

    约定：head 为不存储数据的头结点（哑结点），
    本函数逆置 head.next 起始的数据链表，head 自身位置不变。

    Args:
        head: 链表头结点，允许为 None（此时不做任何操作）。

    注意:
        - 原地修改链表，无返回值（与 list.sort 等就地操作惯例一致）；
        - 时间复杂度 O(n)，空间复杂度 O(1)；
        - 前置条件：链表不得存在环，否则将陷入死循环。
    """
    if head.next is None:
        return

    current = head.next  # 指向第一个待处理的数据结点
    head.next = None  # 摘下原链表，准备头插重建

    while current is not None:
        next_node = current.next  # 先保存后继结点，防止断链
        current.next = head.next  # 头插：将当前结点接到 head 之后
        head.next = current
        current = next_node


# 06_将单链表递增排序
def t06(head: Optional[ListNode]):
    if head.next is None:
        return

    p = head.next
    while p:
        min_node = p
        pn = p.next

        # 寻找最小的节点
        while pn:
            if pn.val < min_node.val:
                min_node = pn
            pn = pn.next

        # 交换节点
        if p != min_node:
            p.val, min_node.val = min_node.val, p.val

        p = p.next


# 08_找出两个单链表的公共节点
# 公共结点：两表同时指向一个节点才叫公共节点，就是两个链表共用一个节点，即从这个节点开始两个链表的数据一定是一模一样的
def t08(L1: Optional[ListNode], L2: Optional[ListNode]) -> Optional[ListNode]:
    # 拿到两个链表的长度
    len1 = LinkedListUtils.get_len(L1.next)
    len2 = LinkedListUtils.get_len(L2.next)

    p1 = L1.next
    p2 = L2.next

    # 就算有公共节点也肯定是在链表的最后面，所以先对齐长度
    while len1 != len2:
        if len1 > len2:
            p1 = p1.next
            len1 -= 1
        else:
            p2 = p2.next
            len2 -= 1

    # 对齐长度后判断，如果是同一个节点，说明从这个节点之后的都是公共节点
    while p1 is not None and p2 is not None and p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1


# 09_按照递增持次序输出带头节点的单链表，并释放该节点，要求空间复杂度为O(1)
def t09(head: Optional[ListNode]):
    if head is None:
        return

    while head.next:
        pre_min = head
        min_node = head.next
        # 从第二个有效节点开始比较，跳过与自身的无效比较
        pre = head.next
        p = head.next.next
        while p:
            if p.val < min_node.val:
                min_node = p
                pre_min = pre
            pre = p
            p = p.next
        # 删除最小节点
        pre_min.next = min_node.next
        print(min_node.val, end=" ")
        min_node.next = None
        del min_node
    del head


# 10_将一个带头节点的单链表A分解为两个带头节点的单链表B，C
# B中储存A中序号为奇数的元素，C中存储A中序号为偶数的元素，且保持相对顺序不变
def t10(head: Optional[ListNode]) -> tuple[Optional[ListNode], Optional[ListNode]]:
    if head is None:
        return None, None

    B = ListNode()
    C = ListNode()

    tb = B
    tc = C

    p = head.next

    while p:
        pn = p.next
        if p.val % 2 == 1:
            tb.next = p
            tb = p
            tb.next = None
        else:
            tc.next = p
            tc = p
            tc.next = None
        p = pn

    # 将原链表置空
    head.next = None
    return B, C


# 11_将带头节点的链表A={a1, b1, a2, b2 …… an, bn}拆分为两个带头节点的单链表
# B = {a1, a2, a3 …… an}
# C = {bn, …… b3, b2, b1}
def t11(head: Optional[ListNode]) -> tuple[Optional[ListNode], Optional[ListNode]]:
    if head is None:
        return None, None

    B = ListNode()
    C = ListNode()

    tb = B
    hc = C

    p = head.next
    count = 1

    while p:
        pn = p.next
        if count % 2 == 1:
            tb.next = p
            tb = p
            tb.next = None
        else:
            p.next = hc.next
            hc.next = p
        p = pn
        count += 1
    # 将原链表置空
    head.next = None
    return B, C


# 15_求A、B两个递增排列的链表的交集，并将结果存放与链表A中，并将其余节点都释放掉
def t15(A: Optional[ListNode], B: Optional[ListNode]):
    prea = A
    preb = B
    pa = A.next
    pb = B.next
    # 若当前pa结点的值小于pb结点的值，删除释放pa指向的结点，pa继续向后推进
    # 若当前pb结点的值小于pa结点的值，删除释放pb指向的结点，pb继续向后推进
    # 若当前pa结点的值等于pb结点的值，删除释放pb指向的结点，pa、pb继续向后推进
    while pa and pb:
        if pa.val < pb.val:
            t = pa
            pa = pa.next
            prea.next = pa
            del t
        elif pa.val > pb.val:
            t = pb
            pb = pb.next
            preb.next = pb
        else:
            t = pb
            pb = pb.next
            preb.next = pb
            del t
            prea = pa
            pa = pa.next
    # 释放残留元素
    while pa:
        t = pa
        pa = pa.next
        prea.next = pa
        del t

    while pb:
        t = pb
        pb = pb.next
        preb.next = pb
        del t

    B.next = None


# 16_有A，B两个链表，判断链表B是否是链表A的子链
def t16(A: Optional[ListNode], B: Optional[ListNode]) -> bool:
    if A is None or B is None:
        return False

    pa = A.next
    pb = B.next

    while pa:
        if pa.val == pb.val:
            pan = pa
            while pan and pb and pan.val == pb.val:
                pan = pan.next
                pb = pb.next
            if pb is None:
                return True
        pa = pa.next
        pb = B.next

    return False


# 25_设线性表L=(a1,a2,a3……an)，采用带头节点的单链表保存，请设计一个空间复杂度为1,且时间上尽可能高效的算法，重新排列L中的各结点，
# 得到线性表L’=(a1,an,a2,an-1,a3,an-2,……)
#      1)算法思想
#          先找到中间结点的前一个结点，将该结点之后的结点就地逆置
#          然后将链表的头结点摘下，链表中前半部分和后半部分的元素分别按照规定尾插到头节点后面
#      2）时间复杂度和空间复杂度
#          时间复杂度：O(n)
#          空间复杂度：O(1)
def t25(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    # 获取链表的长度，计算中间节点的下标
    n = LinkedListUtils.get_len(head.next)
    mid = n // 2

    # 将头节点摘下来
    p1 = p2 = head.next
    head.next = None
    tail = head

    # 找到中间节点的前一个节点，并对后半段链表进行逆置
    for _ in range(mid - 1):
        p2 = p2.next

    # 将前半段链表末尾节点的 next 置为 None，不然会产生死循环
    pn = p2.next
    p2.next = None
    # 新建一个虚拟头节点存储逆置之后的后半段链表
    new_head = ListNode()

    while pn:
        """逆置后半段链表"""
        temp = pn
        pn = pn.next
        temp.next = new_head.next
        new_head.next = temp

    # 后半段链表逆置后的第一个节点
    p2 = new_head.next

    # 交替尾插到 head 后面
    count = 0
    while p1 and p2:
        if count % 2 == 0:
            tail.next = p1
            tail = p1
            p1 = p1.next
        else:
            tail.next = p2
            tail = p2
            p2 = p2.next
        count += 1

    # 清理残余节点
    while p1:
        tail.next = p1
        tail = p1
        p1 = p1.next

    while p2:
        tail.next = p2
        tail = p2
        p2 = p2.next

    # 最后置空
    tail.next = None


if __name__ == "__main__":
    raw_list = [1, 2, 3, 4, 5, 6, 7]
    head = LinkedListUtils.from_list(vals=raw_list, is_head=True)
    t25(head)
    LinkedListUtils.print_list(head)
