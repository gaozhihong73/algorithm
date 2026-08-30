class Solution1:
    """
    暴力解法，挨个比较
    """

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1 or n == 0:
            return s
        max_len = 1
        max_index = [0, 0]
        for i in range(n):
            for j in range(i + 1, n):
                """
                挨个比较，如果当前区间字符串长度 > 目前已知的最长回文串长度，就去判断当前区间字符串
                如果也是回文串，就更新最长回文串长度和下标
                """
                if (j - i + 1) > max_len and self.is_palindromic(s[i : j + 1]):
                    if (j - i + 1) > max_len:
                        max_len = j - i + 1
                        max_index = [i, j]

        return s[max_index[0] : max_index[1] + 1]

    def is_palindromic(self, s: str) -> bool:
        n = len(s)

        left = 0
        right = n - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


class Solution:
    """
    两边探测法
    """

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1 or n == 0:
            return s

        left = right = 0
        a = b = 0
        max_len = 0

        for i in range(n):
            """
            从当前位置向两边扩散，为了覆盖所有样例，所以要区分奇数扩散和偶数扩散
            """
            # 奇数扩散
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # 到此为止 (left, right) 中是从当前位置扩散的最长回文串，不包括下标为 left 的和 right 的元素
            # 所以 长度的计算方式就是 right + left + 1 - 2 = right - left - 1
            l = right - left - 1
            if max_len < l:
                max_len = l
                a = left + 1
                b = right - 1

            # 偶数扩散
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            l = right - left - 1
            if max_len < l:
                max_len = l
                a = left + 1
                b = right - 1

        return s[a : b + 1]


if __name__ == "__main__":
    Solution().longestPalindrome("abbcccba")
