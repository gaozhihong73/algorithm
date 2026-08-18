from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        ans = [0] * n

        if k == 0:
            return ans

        if k > 0:
            left, right = 1, k
        else:
            left, right = n - abs(k), n - 1

        cur_sum = sum(code[left : right + 1])
        ans[0] = cur_sum
        for i in range(1, n):
            cur_sum -= code[left]
            cur_sum += code[(right + 1) % n]
            ans[i] = cur_sum
            left, right = (left + 1) % n, (right + 1) % n

        return ans


if __name__ == "__main__":
    # Solution().decrypt(code=[5, 7, 1, 4], k=3)
    Solution().decrypt(code=[2, 4, 9, 3], k=-2)
