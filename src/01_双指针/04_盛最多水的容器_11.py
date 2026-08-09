from typing import List


class Solution:
    # 单调性
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n == 1:
            return height[0]

        left = 0
        right = n - 1
        max_v = 0

        while(left < right):
            w = right - left
            h = min(height[left], height[right])
            max_v = max(w * h, max_v)
            while left < right and height[right] <= h: 
                right -= 1
            while left < right and height[left] <= h: 
                left += 1
        return max_v

if __name__ == "__main__":
    print(Solution().maxArea([1,2,4,3]))

