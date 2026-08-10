from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n_s = len(s)
        n_p = len(p)
        hash1 = [0] * 26
        hash2 = [0] * 26

        for i in p:
            hash2[ord(i) - ord("a")] += 1

        left = 0
        count = 0
        ans = []

        # 使用 count 判断 是否是异位词
        for right in range(n_s):
            # 窗口尾部字符的索引
            a = ord(s[right]) - ord("a")
            hash1[a] += 1
            if hash1[a] <= hash2[a]:
                count += 1
            if right - left + 1 > n_p:
                # 宽口首部字符的索引
                b = ord(s[left]) - ord("a")
                if hash1[b] <= hash2[b]:
                    count -= 1
                left += 1
                hash1[b] -= 1
            if count == n_p:
                ans.append(left)

        return ans
