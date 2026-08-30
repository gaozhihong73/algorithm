from collections import Counter
from typing import List


class Solution:
    """
    按列比较
    统计每一列字符的个数，如果列字符的个数 != 该列的总字符数，说明这一列中有多个不同的字符
    此时说明匹配失败，返回即可
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None:
            return ""
        n = len(strs)
        if n == 1:
            return strs[0]
        s_len = len(strs[0])
        lookup = Counter()
        ans = ""  # 存储结果
        c = ""  # 存储该列的字符（理论上应该是一样的）
        for i in range(s_len):  # 行（以第个字符串的长度为基准）
            for j in range(n):  # 列
                if (
                    i >= len(strs[j])
                ):  # 如果长度不匹配，说明有的串已经到结尾了，肯定不会有公共子串了，直接返回
                    return ans
                lookup[strs[j][i]] += 1  # 计数
                c = strs[j][i]

            if lookup[c] == n:  # 判断是否合法
                ans += c
                del lookup[c]
            else:
                return ans

        return ans


if __name__ == "__main__":
    Solution().longestCommonPrefix(["flower", "flow", "flight"])
