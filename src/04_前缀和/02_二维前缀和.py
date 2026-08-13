import sys

data = sys.stdin.buffer.read().split()
it = iter(data)

n = int(next(it))
m = int(next(it))
k = int(next(it))

prefix = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        item = int(next(it))
        prefix[i][j] = item + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

for _ in range(k):
    x1 = int(next(it))
    y1 = int(next(it))
    x2 = int(next(it))
    y2 = int(next(it))
    print(
        prefix[x2][y2]
        - prefix[x1 - 1][y2]
        - prefix[x2][y1 - 1]
        + prefix[x1 - 1][y1 - 1]
    )
