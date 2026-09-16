class Solution1:
    """
    模拟，找到所有 a 的下标，按照规则插入
    """

    def isValid(self, s: str) -> bool:
        ans = ""
        n = len(s)
        if n == 0:
            return True
        if n % 3 != 0:
            return False

        index = []

        for i in range(n):
            if s[i] == "a":
                index.append(i)

        for i in index:
            ans = ans[:i] + "abc" + ans[i:]

        return ans == s


class Solution:
    """
    栈，类似于括号匹配
    """

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "a":
                stack.append(c)
            elif c == "b":
                if len(stack) > 0 and stack[-1] == "a":
                    stack.pop()
                    stack.append(c)
                else:
                    return False
            elif c == "c":
                if len(stack) > 0 and stack[-1] == "b":
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
