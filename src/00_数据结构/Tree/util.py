from collections import deque
from typing import List, Optional


class TreeNode:
    """二叉树节点定义（与 LeetCode 标准定义一致）"""

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


class TreeUtils:
    """二叉树辅助工具类：支持 LeetCode 标准层序遍历格式（包含 None）的构建与转换"""

    @staticmethod
    def from_list(vals: List[Optional[int]]) -> Optional[TreeNode]:
        """根据层序遍历列表构建二叉树（例如: [3, 9, 20, None, None, 15, 7]）"""
        if not vals or vals[0] is None:
            return None

        root = TreeNode(vals[0])
        queue = deque([root])
        i = 1
        n = len(vals)

        while queue and i < n:
            curr = queue.popleft()

            # 处理左子节点
            if i < n and vals[i] is not None:
                curr.left = TreeNode(vals[i])
                queue.append(curr.left)
            i += 1

            # 处理右子节点
            if i < n and vals[i] is not None:
                curr.right = TreeNode(vals[i])
                queue.append(curr.right)
            i += 1

        return root

    @staticmethod
    def to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
        """将二叉树转换为 LeetCode 风格的层序列表（去掉末尾多余的 None）"""
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # 移除尾部无意义的 None
        while result and result[-1] is None:
            result.pop()

        return result

    @staticmethod
    def print_tree(
        root: Optional[TreeNode], level: int = 0, prefix: str = "Root: "
    ) -> None:
        """直观地按树形结构打印二叉树（逆时针旋转90度打印，便于终端查看）"""
        if root is not None:
            TreeUtils.print_tree(root.right, level + 1, prefix="R--- ")
            print("    " * level + prefix + str(root.val))
            TreeUtils.print_tree(root.left, level + 1, prefix="L--- ")
