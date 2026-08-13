import sys

# 一次性读取所有数据，按空白分割
data = sys.stdin.buffer.read().split()
it = iter(data)
n = int(next(it))
m = int(next(it))

# 读取数组，构建前缀和（1-based 索引）
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + int(next(it))

for _ in range(m):
    l = int(next(it))
    r = int(next(it))
    print(prefix[r] - prefix[l - 1])
