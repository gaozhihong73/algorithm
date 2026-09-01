from typing import List, Optional


class ListNode:
    """单链表节点定义（与 LeetCode 标准定义一致）"""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        # 方便直接 print(node) 查看当前节点值
        return f"ListNode({self.val})"


class LinkedListUtils:
    """链表辅助工具类：负责数组与链表的相互转换及可视化打印"""

    @staticmethod
    def from_list_nhead(vals: List[int]) -> Optional[ListNode]:
        """根据 Python 列表构建单链表，返回头节点"""
        if not vals:
            return None

        dummy = ListNode(0)  # 虚拟头节点，简化构建逻辑
        curr = dummy
        for val in vals:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    @staticmethod
    def from_list_head(vals: List[int]) -> Optional[ListNode]:
        """根据 Python 列表构建单链表，返回头节点"""
        if not vals:
            return None

        dummy = ListNode(0)  # 虚拟头节点，简化构建逻辑
        curr = dummy
        for val in vals:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy

    @staticmethod
    def to_list(head: Optional[ListNode]) -> List[int]:
        """将链表转换为 Python 列表"""
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    @staticmethod
    def print_list(head: Optional[ListNode], is_head=True) -> None:
        """格式化打印链表结构：1 -> 2 -> 3 -> None"""
        elements = []
        curr = head.next if is_head else head
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        elements.append("None")
        print(" -> ".join(elements))
