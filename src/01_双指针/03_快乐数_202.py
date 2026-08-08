
class Solution:
    # set 列表判断法
    def isHappy(self, n: int) -> bool:
        if n == 2:
            return False
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            sum = 0
            while n > 0:
                sum += pow(n % 10, 2)
                n //= 10
            n = sum

        return n == 1


class Solution2:
    # 快慢指针法
    def isHappy(self, n: int) -> bool:
        def get_next(n: int):
            sum = 0
            while n > 0:
                sum += pow(n%10, 2)
                n //= 10
            return sum
         
        slow = n
        fast = get_next(n)

        while slow != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        
        return slow == 1

if __name__ == "__main__":
    # ==================== 运行测试 ====================
    sol = Solution()
    # 验证快乐数
    print("n = 19:", sol.isHappy(19))  # 输出: True
