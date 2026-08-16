class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0
        left = 0
        l = 0

        vowels = "aeiou"

        for right in range(n):
            # 进窗口
            if s[right] in vowels:
                l += 1

            # 出窗口
            while right - left + 1 > k:
                if s[left] in vowels:
                    l -= 1
                left += 1

            # 更新答案
            max_len = max(max_len, l)

        return max_len
