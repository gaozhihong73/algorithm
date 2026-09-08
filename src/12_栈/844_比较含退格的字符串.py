class Solution:
    """
    从前往后遍历无法预料到后面会出现什么情况，所以：从后往前遍历
    两个字符串都从后往前遍历，碰到#要删除前面的一个字符（注意：# 可能会连续出现，出现几次就得删几个字母）
    跳出删除逻辑和，两个字符串中的指针要么指向一个实际元素，要么为负数（遍历完毕字符串）
    此时 若有一个为负数，检查另一个字符的指针不为负数的话说明两个字符串最后的形态是不一样的，返回false
    若两个都不为负数，检测两个字符串的当前值，若不一样返回false
    若两个都为负数，说明两个子串都遍历完毕了，最后是相等的，返回 true
    """

    def backspaceCompare(self, s: str, t: str) -> bool:
        sl = len(s) - 1
        tl = len(t) - 1
        counts = 0
        countt = 0

        while sl >= 0 or tl >= 0:
            # 处理第一个字符串的 #
            while sl >= 0:
                if s[sl] == "#":
                    counts += 1
                    sl -= 1
                elif counts > 0:
                    counts -= 1
                    sl -= 1
                else:
                    break

            # 处理第二个字符串的 #
            while tl >= 0:
                if t[tl] == "#":
                    countt += 1
                    tl -= 1
                elif countt > 0:
                    countt -= 1
                    tl -= 1
                else:
                    break

            # 处理完毕之后比较
            if sl < 0 and tl < 0:
                return True
            elif sl < 0 or tl < 0:
                return False
            else:
                if s[sl] != t[tl]:
                    return False

            sl -= 1
            tl -= 1

        return True


if __name__ == "__main__":
    Solution().backspaceCompare(s="ab##", t="c#d#")
