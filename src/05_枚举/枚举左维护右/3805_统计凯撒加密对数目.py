from typing import Counter, List


class Solution1:
    """
    暴力解法：时间复杂度O(25*n*每个字符串的长度)
    """

    def countPairs(self, words: List[str]) -> int:
        lookup = Counter()
        ans = 0
        for word in words:
            ans += lookup[word]
            lookup[word] += 1
            word = self.shift_lowercase(word)
            for _ in range(25):
                if word in lookup:
                    ans += lookup[word]
                word = self.shift_lowercase(word)

        return ans

    def shift_lowercase(self, s):
        result = []
        for c in s:
            result.append(chr((ord(c) - ord("a") + 1) % 26 + ord("a")))

        return "".join(result)


class Solution:
    """
    更快一点的解法：将每个字符串都通过 + 1 变为首字母为 'a' 的字符串，这样直接去该搜字符串就行了。
    """

    def countPairs(self, words: List[str]) -> int:
        lookup = Counter()
        ans = 0
        for word in words:
            s = list(word)
            base = ord(s[0]) - ord("a")

            for i in range(len(s)):
                s[i] = chr((ord(s[i]) - base) % 26)

            t = "".join(s)

            ans += lookup[t]

            lookup[t] += 1

        return ans


if __name__ == "__main__":
    Solution().countPairs(["ab", "aa", "za", "aa"])
