# https://leetcode.cn/problems/minimum-window-substring/

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len = len(s)
        t_len = len(t)

        hash1 = Counter()
        hash2 = Counter(t)

        min_len = 10**9
        ans = ""
        count = 0
        left = 0
        for right, item in enumerate(s):
            hash1[item] += 1
            if item in hash2 and hash1[item] <= hash2[item]:
                count += 1

            # 如果符合条件
            while count == t_len:
                # 更新结果
                cur_len = right - left + 1
                if cur_len < min_len:
                    min_len = cur_len
                    ans = s[left : right + 1]

                # 出窗口
                if hash1[s[left]] <= hash2[s[left]]:
                    count -= 1
                hash1[s[left]] -= 1
                left += 1

        return "" if min_len == 10**9 else ans
