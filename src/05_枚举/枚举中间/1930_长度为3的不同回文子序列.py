from typing import Counter


class Solution:
    """
    遍历和中间，维护两边
    """

    def countPalindromicSubsequence(self, s: str) -> int:
        ans = set()
        suf = Counter(list(s))
        pre = set()

        for c in s:
            suf[c] -= 1
            if suf[c] == 0:
                del suf[c]
            for key in pre:
                if key in suf:
                    ans.add("".join([key, c, key]))
            pre.add(c)

        return len(ans)
