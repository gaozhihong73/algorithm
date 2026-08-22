from typing import Counter, List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        lookup = Counter()
        ans = 0

        for elem in rectangles:
            ans += lookup[elem[0] / elem[1]]
            lookup[elem[0] / elem[1]] += 1

        return ans


if __name__ == "__main__":
    Solution().interchangeableRectangles(
        rectangles=[[4, 8], [3, 6], [10, 20], [15, 30]]
    )
