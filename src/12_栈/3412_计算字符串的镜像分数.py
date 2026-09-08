from collections import defaultdict


class Solution:
    """
    注意：可能存在相同字符串的问题，所以存储的时候遇到相同的字符串都要存储，不可以覆盖
    """

    def calculateScore(self, s: str) -> int:
        ans = 0
        lookup = defaultdict(list)

        for i in range(len(s)):
            idx = ord(s[i]) - ord("a")
            mirror_idx = 25 - idx  # 镜像字符的索引
            if len(lookup[mirror_idx]) > 0:  # 如果存在镜像字符
                ans += i - lookup[mirror_idx].pop()
            else:
                lookup[idx].append(i)  # 没有匹配，存入当前字符

        return ans


if __name__ == "__main__":
    Solution().calculateScore("aczzx")
