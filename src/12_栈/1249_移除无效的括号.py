class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # 记录左括号的下标
        temp = list(s)
        n = len(s)
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                """
                碰到右括号时，如果有左括号时，左括号出栈
                如果没有左括号，说明当前右括号多余，标记为#，最后删除
                """
                if stack:
                    stack.pop()
                else:
                    temp[i] = "#"

        # 检查栈中是否有多余的左括号
        for i in stack:
            temp[i] = "#"

        # 将所有标记为 # 的元素都删除
        return "".join([t for t in temp if t != "#"])
