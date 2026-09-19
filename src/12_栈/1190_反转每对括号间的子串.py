class Solution:
    """
    记录每一个左括号的位置，加入栈中，遇到右括号时找到最近一个左括号的位置翻转这个区间内的字符即可，处理完整个字符串后最后在字符串中把左右括号都移除即可
    """

    def reverseParentheses(self, s: str) -> str:
        stack = []  # 存储左括号的下标
        s = list(s)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i + 1)
            elif s[i] == ")":
                s[stack[-1] : i] = s[stack[-1] : i][::-1]
                stack.pop()

        return "".join([c for c in s if c != "(" and c != ")"])


if __name__ == "__main__":
    Solution().reverseParentheses(s="(u(love)i)")
