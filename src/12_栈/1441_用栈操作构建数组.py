from typing import List


class Solution:
    """
    简单模拟
    """

    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = [str]
        num = 1
        i = 0

        while i < len(target):
            if num == target[i]:
                ans.append("Push")
                i += 1
                num += 1
            else:
                ans.append("Push")
                ans.append("Pop")
                num += 1
        return ans
