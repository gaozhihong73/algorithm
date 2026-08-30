class KMP:
    def bf(self, S: str, T: str) -> int:
        """
        暴力匹配算法（Brute Force）
        时间复杂度：O(m*n)，其中m和n分别是主串和模式串的长度
        """
        s_len = len(S)  # 主串长度
        t_len = len(T)  # 模式串长度
        i = j = 0  # i指向主串当前比较位置，j指向模式串当前比较位置

        # 当i未超出主串且j未超出模式串时继续匹配
        while i < s_len and j < t_len:
            if S[i] == T[j]:
                # 当前字符匹配成功，两个指针同时后移
                i += 1
                j += 1
            else:
                # 匹配失败，主串指针回溯到本次匹配起始位置的下一个字符
                # j回溯到0（模式串开头）
                i = i - j + 1
                j = 0

        # 如果j等于模式串长度，说明匹配成功，返回起始位置；否则返回-1
        if j == t_len:
            return i - j  # i - j 就是本次匹配在主串中的起始索引
        else:
            return -1

    def get_next(self, T: str) -> list:
        """
        计算next数组（未优化版）
        next[i] 表示模式串T中，以位置i-1结尾的子串（即T[0..i-1]）的最长相等前后缀长度。
        next[0] = -1 为特殊标记，表示不存在前后缀。
        注意：数组长度为 t_len+1，因为循环中i会增加到t_len，需要访问next[t_len]。
        """
        t_len = len(T)
        next = [0] * (t_len + 1)  # 多分配一个位置，避免越界
        next[0] = -1  # 第一个位置特殊处理，表示不存在前后缀

        i = 0  # i指向当前正在处理的字符位置（也代表已匹配前缀的末尾后一位）
        j = -1  # j表示当前最长相等前后缀的长度减1（即前缀末尾的索引）

        while i < t_len:  # 遍历模式串的每个字符，计算next[i+1]
            if j == -1 or T[i] == T[j]:
                # 情况1：j == -1 说明需要重新开始比较（没有可回溯的前缀）
                # 情况2：当前字符匹配成功，前后缀可以延长
                i += 1
                j += 1
                # 此时i和j都后移，新的j就是位置i处的最长相等前后缀长度
                next[i] = j
            else:
                # 匹配失败，回溯j，利用已经计算好的next值快速跳过不可能匹配的位置
                j = next[j]

        return next

    def get_nextval(self, T: str) -> list:
        """
        计算nextval数组（优化版next）
        在next的基础上进一步优化：如果T[i]与T[next[i]]相同，则回溯时仍会匹配失败，
        因此可以直接继承nextval[next[i]]，避免多余的比较。
        数组长度为 t_len，因为循环条件改为 i < t_len - 1，最大i不会达到t_len。
        """
        t_len = len(T)
        nextval = [0] * t_len  # 只需要t_len长度，因为不会访问到索引t_len
        nextval[0] = -1  # 第一个位置特殊处理

        i = 0
        j = -1
        while i < t_len - 1:  # 注意：循环到倒数第二个字符即可，因为计算的是nextval[i+1]
            if j == -1 or T[i] == T[j]:
                i += 1
                j += 1
                # 优化点：判断T[i]和T[j]是否相等
                if T[i] != T[j]:
                    # 如果不等，则正常记录j
                    nextval[i] = j
                else:
                    # 如果相等，则回溯后的字符仍然相同，必然再次失配
                    # 所以直接继承nextval[j]，进一步减少回溯次数
                    nextval[i] = nextval[j]
            else:
                j = nextval[j]  # 回溯

        return nextval

    def kmp(self, S: str, T: str) -> int:
        """
        KMP匹配算法
        利用next或nextval数组避免主串指针回溯，时间复杂度O(m+n)
        """
        s_len = len(S)
        t_len = len(T)
        i = j = 0

        # 计算模式串的next数组（这里选择nextval，更高效）
        # next = self.get_next(T)      # 也可以使用未优化版
        next = self.get_nextval(T)  # 使用优化版nextval

        while i < s_len and j < t_len:
            # 情况1: j == -1，说明模式串需要从头开始匹配（等价于暴力法中的j=0）
            # 情况2: 当前字符匹配成功
            # 这两种情况都需要同时移动 i 和 j
            if j == -1 or S[i] == T[j]:
                i += 1
                j += 1
            else:
                # 匹配失败，模式串指针根据next数组回溯，主串指针i不动
                j = next[j]

        # 如果j等于模式串长度，说明匹配成功
        if j == t_len:
            return i - j  # 返回匹配起始位置
        else:
            return -1


if __name__ == "__main__":
    # 测试数据
    S = "ababcabcacbab"
    T = "abcac"

    # 创建KMP对象并调用kmp方法
    result = KMP().kmp(S, T)
    print("模式串在主串中的位置:", result)  # 预期输出: 5
