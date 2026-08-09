from typing import List


class Solution:
    def twoSum(self, price: List[int], target: int) -> List[int]:
        price.sort()
        n = len(price)
        if price[0] > target:
            return []
        left = 0 
        right = n - 1

        while price[right] > target: 
            right -= 1

        while left < right:
            if price[left] + price[right] > target:
                right -= 1
            elif price[left] + price[right] < target:
                left += 1
            else:
                return [price[left], price[right]]
        return []
