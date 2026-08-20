class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        count = [0] * 26

        max_len = 0
        left = 0

        for right in range(n):
            i = ord(s[right]) - ord("a")
            count[i] += 1

            while count[i] > 2:
                j = ord(s[left]) - ord("a")
                count[j] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
