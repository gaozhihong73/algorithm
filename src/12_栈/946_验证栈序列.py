from typing import List


class Solution:
    """
    使用 列表 模拟栈的操作
    如果当前栈为空 或者 栈顶元素不等于 popped 中的当前元素，入栈
    否则出栈，popped 指针向后一位，也就是说当前位置的出栈元素是正确的

    遍历完毕后检查栈中是否有残留元素，如果有的话与出栈元素列表里面的数据一一比较，如果都相同说明出栈序列没问题，否则返回False
    """

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [pushed[0]]
        i = 1
        top = 0
        j = 0
        n = len(pushed)

        while i < n and j < n:
            if top == -1 or stack[top] != popped[j]:
                stack.append(pushed[i])
                top += 1
                i += 1
            else:
                j += 1
                stack.pop()
                top -= 1

        while j < n and top > 0:
            if stack[top] != popped[j]:
                return False
            else:
                stack.pop()
                top -= 1
                j += 1

        return True


if __name__ == "__main__":
    Solution().validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1])
