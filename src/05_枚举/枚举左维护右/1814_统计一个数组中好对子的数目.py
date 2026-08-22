from typing import Counter, List


class Solution:
    """
    根据题意要考虑三个因素，当前数和当前数的rev，别的数和别的数的rev，数和rev的关系，是一个多对多的关系，需要想办法把三个条件转化为两个条件
    题中给出了符合条件的公式为： nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
    根据移项可得：nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
    这样的话就变成自己和自己计算，只需要计算当前数和当前数的rev，然后去 哈希表中找即可，变成了一对多的关系

    """

    def countNicePairs(self, nums: List[int]) -> int:
        lookup = Counter()
        ans = 0

        for num in nums:
            rev = int(str(num)[::-1])
            ans += lookup[num - rev]
            lookup[num - rev] += 1

        return ans % (10**9 + 7)


if __name__ == "__main__":
    ans = Solution().countNicePairs(
        [352171103, 442454244, 42644624, 152727101, 413370302, 293999243]
    )
    print(ans)
