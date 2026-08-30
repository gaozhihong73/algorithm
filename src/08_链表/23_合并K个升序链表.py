# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    """
    暴力解法：每次都在所有链表头部找出最小的节点，然后尾插到新链表中
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None:
            return lists
        n = len(lists)
        if n == 1:
            return lists[0]
        h = ListNode()
        tail = h
        while True:
            min_index = -1
            for i in range(0, n):
                if lists[i] == None:
                    continue
                if min_index == -1 or lists[min_index].val > lists[i].val:
                    min_index = i

            if min_index == -1:
                break

            tail.next = lists[min_index]
            tail = lists[min_index]

            lists[min_index] = lists[min_index].next

        return h.next


class Solution:
    """
    采用小根堆来实现， 基本用法如下
        import heapq

        # 创建一个空堆
        heap = []

        # 向堆中添加元素
        heapq.heappush(heap, 3)
        heapq.heappush(heap, 1)
        heapq.heappush(heap, 4)
        heapq.heappush(heap, 2)

        # 弹出最小元素
        print(heapq.heappop(heap))  # 输出: 1
        print(heapq.heappop(heap))  # 输出: 2
        注意：
            ListNode 类型无法直接比较，所以我们可以往小根堆里面存储元组 (node.val, node)
            但是如果 node.val 重复，又会去比较元组中的第二个元素 node 还是会报错
            所以我们可以存储一个三元组, 第二个元素存储一个唯一值，或者下标，保证不重复就行，(node.val, id(node), node)
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None:
            return lists
        n = len(lists)
        if n == 1:
            return lists[0]

        heap = []

        for i in range(n):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, id(lists[i]), lists[i]))
                lists[i] = lists[i].next

        h = ListNode()
        tail = h

        while heap:
            _, _, node = heapq.heappop(heap)
            tail.next = node
            tail = node
            if node.next:
                heapq.heappush(heap, (node.next.val, id(node.next), node.next))

        return h.next
