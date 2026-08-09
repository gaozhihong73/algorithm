

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        if n < 3:
            return 0

        for i in range(n-1, 1, -1): # [2, n-1] 倒序
            left = 0
            right = i - 1
            # 确保当前边与除了最大边之外的所有边都匹配一次， 所以此次需要循环
            while left < right:
                if(nums[left] + nums[right] > nums[i]):
                    ans += right - left
                    right -= 1
                else:
                    left += 1
                    
        return ans


if __name__ == "__main__":
    print(Solution().triangleNumber([2,2,3,4]))

