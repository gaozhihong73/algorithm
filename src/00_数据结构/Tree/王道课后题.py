from typing import Optional

from tree_util import TreeNode, TreeUtils


# 寻找公共祖先
def lac(
    root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
) -> Optional[TreeNode]:
    """
    寻找节点 p 和 q 的最近公共祖先 (LCA)
    :param root: 树的根节点
    :param p: 目标节点 p
    :param q: 目标节点 q
    :return: 最近公共祖先节点
    """
    # 1. 递归终止条件：
    # 如果遍历到空节点，或者找到了 p 或 q 本身，直接返回当前节点
    if root is None or root == p or root == q:
        return root

    # 2. 递归查找：分别在左子树和右子树寻找 p 和 q
    left = lac(root.left, p, q)
    right = lac(root.right, p, q)

    # 3. 结果合并：
    # 如果左、右子树各找到一个节点，说明当前 root 就是最近公共祖先
    if left is not None and right is not None:
        return root

    # 如果只有一侧找到了目标节点，返回找到的那一侧结果；两侧都没找到则返回 None
    return right if left is None else left


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7]
    root = TreeUtils.from_list(vals=nodes)
    ans = lac(root, root.right.right, root.right.left)
    TreeUtils.print_tree(root=ans)
