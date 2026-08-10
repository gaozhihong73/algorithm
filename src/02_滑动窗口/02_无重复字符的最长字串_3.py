class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        hh = set()
        max_len = -1
        left = 0

        for right in range(n):
            while s[right] in hh:
                hh.remove(s[left])
                left += 1
            max_len = max(max_len, right - left + 1)
            hh.add(s[right])

        return 0 if max_len == -1 else max_len
