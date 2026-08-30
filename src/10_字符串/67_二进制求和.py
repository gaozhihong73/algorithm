class Solution:
    def addBinary(self, a: str, b: str) -> str:
        al = len(a) - 1
        bl = len(b) - 1

        ans = ""

        cur = 0
        while al >= 0 or bl >= 0:
            x = 0 if al < 0 else ord(a[al]) - ord("0")
            y = 0 if bl < 0 else ord(b[bl]) - ord("0")
            s = x + y + cur
            ans += str(s % 2)
            cur = s // 2
            al -= 1
            bl -= 1

        if cur != 0:
            ans += str(cur)

        return ans[::-1]


if __name__ == "__main__":
    Solution().addBinary(a="11", b="1")
