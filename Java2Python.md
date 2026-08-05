## 1. 数组与二维数组 (Array / 2D Array)

在 Java 中需要使用 `new` 关键字并指定长度，而在 Python 中，数组（列表 List）是动态的，通常使用**乘法或列表推导式**来初始化固定长度。

| 功能                | Java 语法                            | Python 3 语法                      |
| ------------------- | ------------------------------------ | ---------------------------------- |
| **一维数组初始化**  | `int[] dp = new int[n];`             | `dp = [0] * n`                     |
| **二维数组初始化**  | `int[][] dp = new int[m][n];`        | `dp = [[0] * n for _ in range(m)]` |
| **获取数组长度**    | `arr.length`                         | `len(arr)`                         |
| **获取矩阵行/列数** | `matrix.length` / `matrix[0].length` | `len(matrix)` / `len(matrix[0])`   |

```python
# 1. 一维数组初始化：创建一个长度为 n，初始值全为 0 的一维数组
n = 5
arr = [0] * n  

# 2. 二维数组初始化：创建一个 m 行 n 列的二维数组（常用于动态规划 dp 表）
m = 3
dp = [[0] * n for _ in range(m)] 

# ⚠️ 致命避坑警告：千万不要用 dp = [[0] * n] * m 初始化二维数组！
# 这种写法会导致多行引用同一个一维数组，修改 dp[0][0] 时，dp[1][0] 也会跟着变。
# 必须使用列表推导式 for _ in range(m) 来确保每一行都是独立的新列表。

```

## 2. 哈希表 (HashMap)

Python 的内置字典 `dict` 底层就是高度优化的哈希表。

| 功能               | Java 语法                                | Python 3 语法                       |
| ------------------ | ---------------------------------------- | ----------------------------------- |
| **初始化**         | `Map<K, V> map = new HashMap<>();`       | `hash_map = {}` 或 `dict()`         |
| **存入键值对**     | `map.put(key, val);`                     | `hash_map[key] = val`               |
| **判断包含 Key**   | `map.containsKey(key);`                  | `key in hash_map`                   |
| **获取值及默认值** | `map.getOrDefault(key, 0);`              | `hash_map.get(key, 0)`              |
| **遍历键值对**     | `for(Map.Entry<K,V> e : map.entrySet())` | `for key, val in hash_map.items():` |

```python
hash_map = {}

# 1. 存入与更新数据
hash_map["apple"] = 1

# 2. 安全获取数据：如果键不存在，返回默认值 0
count = hash_map.get("banana", 0)

# 3. 统计频次的标准写法（对应 Java 的 map.put(k, map.getOrDefault(k,0)+1)）
hash_map["apple"] = hash_map.get("apple", 0) + 1

# 4. 遍历哈希表
for key, value in hash_map.items():
    print(key, value)

```

> **高阶技巧**：Python 提供了 `collections.defaultdict(int)`，调用不存在的 key 时会自动初始化为 0，连 `get` 都省了，写算法极其方便。

## 3. 集合 (HashSet)

用于去重或者快速查找 O(1) 存在性。

| 功能         | Java 语法                             | Python 3 语法                           |
| ------------ | ------------------------------------- | --------------------------------------- |
| **初始化**   | `Set<Integer> set = new HashSet<>();` | `hash_set = set()`                      |
| **添加元素** | `set.add(val);`                       | `hash_set.add(val)`                     |
| **判断包含** | `set.contains(val);`                  | `val in hash_set`                       |
| **删除元素** | `set.remove(val);`                    | `hash_set.remove(val)` / `discard(val)` |

```python
# 1. 初始化空集合（注意不能用 {}，那代表空字典）
hash_set = set()

# 2. 初始化并去重（直接将列表转为集合）
nums = [1, 2, 2, 3]
unique_set = set(nums)  # 结果为 {1, 2, 3}

# 3. 添加与判断
hash_set.add(5)
if 5 in hash_set:
    hash_set.remove(5) # 若元素不存在会报错，安全删除可以用 hash_set.discard(5)
```

## 4. 字符串 (String)

Python 字符串和 Java 一样是**不可变**的。

| 功能              | Java 语法                         | Python 3 语法                        |
| ----------------- | --------------------------------- | ------------------------------------ |
| **获取指定字符**  | `s.charAt(i)`                     | `s[i]`                               |
| **截取子串**      | `s.substring(i, j)`               | `s[i:j]` (切片操作)                  |
| **转字符数组**    | `s.toCharArray()`                 | `list(s)`                            |
| **StringBuilder** | `StringBuilder sb; sb.append(c);` | `sb = []; sb.append(c); "".join(sb)` |

```python
s = "abcdef"

# 1. 截取子串（切片）：获取下标从 i 到 j-1 的字符串，等价于 s.substring(1, 4)
sub = s[1:4] # 结果为 "bcd"

# 2. 替代 StringBuilder：因为 Python 字符串拼接 "+" 效率低，
# 通常先用列表(List)收集字符，最后使用 join 拼接
sb = []
sb.append("a")
sb.append("b")
result = "".join(sb) # 将列表中的字符全部拼成一个字符串，结果为 "ab"

# 3. 翻转字符串（切片的高级用法）
reversed_s = s[::-1] # 结果为 "fedcba"

```

---

### 5. 栈与双端队列 (Stack & Deque)

Python 没有原生的 `Stack` 类，直接用列表 `List` 模拟。队列使用 `collections.deque`。

| 功能              | Java 语法                                | Python 3 语法                                |
| ----------------- | ---------------------------------------- | -------------------------------------------- |
| **栈初始化**      | `Stack<Integer> st = new Stack<>();`     | `stack = []`                                 |
| **压栈/弹栈**     | `st.push(x); st.pop();`                  | `stack.append(x); stack.pop();`              |
| **查看栈顶**      | `st.peek();`                             | `stack[-1]`                                  |
| **队列初始化**    | `Deque<Integer> q = new ArrayDeque<>();` | `from collections import deque; q = deque()` |
| **队尾入/队首出** | `q.offer(x); q.poll();`                  | `q.append(x); q.popleft();`                  |

```python
from collections import deque

# --- 栈 (Stack) ---
stack = []
stack.append(1) # 压栈
stack.append(2)
top = stack[-1] # 查看栈顶元素 (2)，前提是 stack 不为空
val = stack.pop() # 弹栈，移除并返回 2

# --- 队列 (Queue / BFS 必备) ---
q = deque()
q.append(1) # 元素从右侧入队
q.append(2)
first = q.popleft() # 元素从左侧出队 (1)，时间复杂度 O(1)

```

---

### 6. 优先队列 / 堆 (PriorityQueue)

Python 内置了 `heapq` 模块，**默认只提供小顶堆**。

| 功能             | Java 语法                          | Python 3 语法                 |
| ---------------- | ---------------------------------- | ----------------------------- |
| **小顶堆初始化** | `PriorityQueue<Int> pq = new...`   | `import heapq; pq = []`       |
| **入堆**         | `pq.offer(x);`                     | `heapq.heappush(pq, x)`       |
| **出堆**         | `pq.poll();`                       | `heapq.heappop(pq)`           |
| **大顶堆**       | `new PriorityQueue<>((a,b)->b-a);` | 存入相反数 `-x`，取出时再取反 |

```python
import heapq

# 1. 小顶堆使用
min_heap = []
heapq.heappush(min_heap, 5) # 将元素推入堆中
heapq.heappush(min_heap, 1)
min_val = heapq.heappop(min_heap) # 弹出堆顶最小元素，返回 1

# 2. 大顶堆的巧妙实现：将数字乘 -1 存入，利用小顶堆的特性反向排序
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -1)
max_val = -heapq.heappop(max_heap) # 弹出 -5，再加个负号还原成最大值 5

# 3. 存入复杂对象（类似 Java 自定义 Comparator）
# Python 堆可以存元组，默认会按照元组的第一个元素进行排序
pq = []
heapq.heappush(pq, (3, "apple"))  # 3 作为排序权重
heapq.heappush(pq, (1, "banana"))
weight, fruit = heapq.heappop(pq) # 弹出 (1, "banana")

```

---

### 7. 循环与自增自减运算符 (for / i++ / ++i)

Python **没有** `i++`、`++i`、`--i` 这类自增自减运算符，必须显式写 `i += 1`。

| 功能                     | Java 语法                                        | Python 3 语法                          |
| ------------------------ | ------------------------------------------------ | -------------------------------------- |
| **普通递增循环**         | `for (int i = 0; i < n; i++)`                    | `for i in range(n):`                   |
| **倒序循环**             | `for (int i = n - 1; i >= 0; i--)`               | `for i in range(n - 1, -1, -1):`       |
| **带步长循环**           | `for (int i = k; i < n; i += d)`                 | `for i in range(k, n, d):`             |
| **增强 for（遍历元素）** | `for (int num : nums)`                           | `for num in nums:`                     |
| **遍历字符串字符**       | `for (char c : s.toCharArray())`                 | `for c in s:`                          |
| **自增操作**             | `i++;` / `++i;`                                  | `i += 1`                               |
| **表达式内的自增**       | `nums[left++]` 等（先取值再自增，见下方避坑）    | 必须拆成两步                       |

```python
# 1. 普通递增循环：等价于 for (int i = 0; i < n; i++)
for i in range(n):
    print(i)

# 2. 倒序循环：等价于 for (int i = n - 1; i >= 0; i--)
for i in range(n - 1, -1, -1):
    print(i)

# 3. 增强 for：直接遍历数组元素（无需下标）
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

# 4. 遍历字符串的每个字符：等价于 for (char c : s.toCharArray())
s = "hello"
for c in s:
    print(c)  # 直接得到字符，无需 s.charAt(i)
```

> **⚠️ 致命避坑警告：自增自减在表达式中无法直接翻译**
> Java 里 `while (i < n && nums[i++] == x)` 这类「后置自增」写法在 Python 中不存在，
> 必须显式拆成两步，否则逻辑会错乱：

```java
// Java 原文：sum -= nums[left++];  // 先取出 nums[left] 做减法，再让 left 加一
```

```python
# Python 等价写法：必须拆成两步
sum -= nums[left]
left += 1
```

---

### 8. 极值常量与 Math 工具类

| 功能                    | Java 语法                         | Python 3 语法                |
| ----------------------- | --------------------------------- | ---------------------------- |
| **正无穷（作最小值）**  | `Integer.MAX_VALUE`               | `float("inf")` 或 `10**9`    |
| **负无穷（作最大值）**  | `Integer.MIN_VALUE`               | `-float("inf")` 或 `-10**9`  |
| **自定义极小值**        | `-0x3f3f3f3f`                     | `-0x3f3f3f3f`（直接照抄即可）|
| **最大值**              | `Math.max(a, b)`                  | `max(a, b)`                  |
| **最小值**              | `Math.min(a, b)`                  | `min(a, b)`                  |
| **绝对值**              | `Math.abs(x)`                     | `abs(x)`                     |
| **开平方**              | `Math.sqrt(x)`                    | `x ** 0.5` 或 `import math; math.sqrt(x)` |

```python
# 1. 初始化一个「很大」的变量，用于后续取最小值（等价于 Integer.MAX_VALUE）
min_len = float("inf")
if 5 < min_len:
    min_len = 5

# 2. 多个值取最大/最小：max 和 min 天然支持多参数，无需嵌套调用
# Java 的 Math.min(Math.min(a, b), c) 在 Python 中直接写 min(a, b, c)
result = min(dp[i - 1][j], dp[i][j - 1])  # 等价于 Math.min(dp[i-1][j], dp[i][j-1])

# 3. 动态规划中常用 -inf 表示「不可达状态」
dp = [-float("inf")] * n
```

---

### 9. 字符运算与字符串高级操作

| 功能                     | Java 语法                              | Python 3 语法                          |
| ------------------------ | -------------------------------------- | -------------------------------------- |
| **取指定字符**           | `s.charAt(i)`                          | `s[i]`                                 |
| **字符转数字**           | `c - '0'`                              | `ord(c) - ord('0')` 或 `int(c)`        |
| **字母转下标**           | `cs['c' - 'a']`                        | `cnt[ord(c) - ord('a')]`               |
| **判断是数字字符**       | `c >= '0' && c <= '9'`                 | `'0' <= c <= '9'`                      |
| **字符数组转字符串**     | `String.valueOf(cs)`                   | `"".join(cs)`                          |
| **字符串反转**           | `new StringBuilder(s).reverse().toString()` | `s[::-1]`                          |
| **截取子串**             | `s.substring(a, b)`（含a不含b）        | `s[a:b]`（含a不含b）                   |
| **转字符数组**           | `s.toCharArray()`                      | `list(s)`                              |
| **字符数组排序**         | `Arrays.sort(cs)`                      | `cs.sort()`（list 才能 sort）          |
| **字符串比较**           | `s.equals(t)`                          | `s == t`                               |
| **拼接数字与字符串**     | `sb.append(count)`                     | `sb.append(str(count))`（list 内要转字符串）|

```python
s = "abc123"

# 1. 逐个字符处理，将数字字符转换为对应整数（等价于 c - '0'）
for c in s:
    if '0' <= c <= '9':          # 等价于 c >= '0' && c <= '9'
        num = ord(c) - ord('0')  # 等价于 c - '0'
        print(num)

# 2. 使用下标索引字符，配合 ord 做「字母频次统计」
# Java: cs['c' - 'a']++  对应  Python: cnt[ord('c') - ord('a')] += 1
cnt = [0] * 26
for c in s.lower():
    if 'a' <= c <= 'z':
        cnt[ord(c) - ord('a')] += 1  # 等价于 cs[c - 'a']++

# 3. 字符数组排序后转回字符串（异位词分组的核心技巧）
# Java: char[] cs = str.toCharArray(); Arrays.sort(cs); strSort = String.valueOf(cs);
str = "bca"
cs = list(str)        # 等价于 str.toCharArray()，得到 ['b', 'c', 'a']
cs.sort()             # 等价于 Arrays.sort(cs)
str_sort = "".join(cs) # 等价于 String.valueOf(cs)，结果为 "abc"

# 4. 字符串反转：切片 [::-1] 一步搞定，等价于 Java 的 StringBuilder(s).reverse()
reversed_s = s[::-1]
```

> **注意**：Java 的 `char` 是整数类型，可以直接做减法 `c - 'a'`；
> Python 的字符是字符串类型，必须先经过 `ord()` 转成 Unicode 码点才能做算术运算。

---

### 10. 排序与数组工具 (Arrays)

| 功能                       | Java 语法                                            | Python 3 语法                        |
| -------------------------- | ---------------------------------------------------- | ------------------------------------ |
| **数组排序（原地）**       | `Arrays.sort(nums)`                                  | `nums.sort()`                        |
| **数组排序（新副本）**     | `Arrays.copyOf` + sort（较繁琐）                     | `sorted(nums)`                       |
| **数组填充**               | `Arrays.fill(dp, 1)`                                 | `dp = [1] * n`                       |
| **转成 List**              | `Arrays.asList(a, b, c)`                             | `[a, b, c]`                          |
| **数组转字符串打印**       | `Arrays.toString(nums)`                              | `str(nums)`                          |
| **二维数组按某列排序**     | `Arrays.sort(pairs, (a,b) -> a[0] - b[0])`           | `pairs.sort(key=lambda x: x[0])`     |

```python
nums = [3, 1, 2]

# 1. 原地排序：等价于 Arrays.sort(nums)
nums.sort()                     # nums 变为 [1, 2, 3]

# 2. 不修改原数组的排序（返回新列表）：Python 刷题常用
nums2 = [3, 1, 2]
sorted_nums = sorted(nums2)     # nums2 不变，sorted_nums 为 [1, 2, 3]

# 3. 数组填充初始化：等价于 Arrays.fill(dp, 1)
dp = [1] * n

# 4. 二维数组按照子数组的第一个元素排序（区间类题常用）
pairs = [[5, 8], [1, 3], [2, 6]]
pairs.sort(key=lambda x: x[0])  # 按 x[0] 升序
pairs.sort(key=lambda x: x[0], reverse=True)  # 按 x[0] 降序
```

> **⚠️ 避坑警告**：`nums.sort()` 是原地排序返回 `None`，千万不要写成
> `nums = nums.sort()`，那样会得到 `None`！需要新列表才用 `sorted(nums)`。

---

### 11. 位运算补充 (Bitwise)

位运算符在 Java 和 Python 中符号**基本一致**：`^` 异或、`&` 与、`|` 或、`<<` 左移、`>>` 右移、`~` 取反。

| 功能                     | Java 语法                                  | Python 3 语法              |
| ------------------------ | ------------------------------------------ | -------------------------- |
| **异或（无进位相加）**   | `a ^ b`                                    | `a ^ b`                    |
| **取最低位 1**           | `x & (-x)`                                 | `x & (-x)`                 |
| **清除最低位 1**         | `n &= (n - 1)`                             | `n &= n - 1`               |
| **判断某位是否为 1**     | `(num & lsb) != 0`                         | `(num & lsb) != 0`         |
| **统计二进制 1 的个数**  | `Integer.bitCount(x)`                      | `bin(x).count("1")` 或 `x.bit_count()` |
| **转二进制字符串**       | `Integer.toBinaryString(x)`                | `bin(x)`（带前缀 "0b"）    |

```python
# 1. 异或运算：找出只出现一次的数字（所有出现两次的数异或后抵消为 0）
a, b = 4, 7
result = a ^ b

# 2. 提取最右侧的 1：常用于「只出现一次的数字Ⅲ」将数组分成两组
x = 12          # 二进制 1100
lsb = x & (-x)  # 结果为 4（二进制 100），即最右侧那个 1

# 3. 清除最低位的 1：用于统计二进制中 1 的个数
n = 12          # 二进制 1100，有 2 个 1
count = 0
while n > 0:
    n &= n - 1  # 等价于 n &= (n - 1)，每次去掉一个 1
    count += 1
print(count)    # 输出 2

# 4. 快速统计 1 的个数：等价于 Integer.bitCount(x)
x = 12
bit_count = bin(x).count("1")  # Python 3.10+ 也可用 x.bit_count()
```

> **⚠️ 避坑警告**：Java 的 `int` 是 32 位有符号整数，溢出会回绕；
> Python 的整数是**任意精度**的，负数用补码表示时概念上有无限个前导 1，
> 因此极少数涉及「无符号右移 >>>」或「溢出回绕」的题（如 `两整数之和_371`）
> 需要手动加 `& 0xFFFFFFFF` 来模拟 32 位溢出，刷题时留意即可。

---

### 12. 链表 ListNode 定义与使用

| 功能                   | Java 语法                       | Python 3 语法              |
| ---------------------- | ------------------------------- | -------------------------- |
| **定义链表节点**       | `class ListNode { int val; ListNode next; }` | 见下方 `class ListNode` |
| **创建节点**           | `new ListNode(0)`               | `ListNode(0)`              |
| **访问属性**           | `node.val` / `node.next`        | `node.val` / `node.next`   |
| **判空**               | `head == null`                  | `head is None` 或 `not head` |

```python
# 链表节点的标准定义（等价于 ListNode.java）
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # 节点值
        self.next = next    # 指向下一个节点的引用，默认 None

# 1. 创建虚拟头节点（dummy node）：等价于 ListNode newHead = new ListNode(0)
dummy = ListNode(0)
tail = dummy

# 2. 遍历链表：等价于 while (p != null)
p = dummy
while p is not None:
    p = p.next
# 或简写为：
while p:
    p = p.next

# 3. 判断节点是否为空：等价于 if (head == null || head.next == null)
if head is None or head.next is None:
    return
```

> **提示**：刷题时 Python 解法不需要写完整的 ListNode 类，直接引用即可（LeetCode 环境已内置），
> 但本地测试需要先定义这个类。

---

### 13. 输入输出 (Scanner / System.out)

| 功能                    | Java 语法                                  | Python 3 语法                     |
| ----------------------- | ------------------------------------------ | --------------------------------- |
| **读整数**              | `Scanner in = new Scanner(System.in); in.nextInt()` | `int(input())`            |
| **读字符串**            | `in.next()`                                | `input()`                        |
| **循环读多个 case**     | `while (in.hasNextInt())`                  | `while True: try: ... except:` 或一次性读取 |
| **输出并换行**          | `System.out.println(x)`                    | `print(x)`                       |
| **输出不换行**          | `System.out.print(x + " ")`                | `print(x, end=" ")`              |

```python
# 1. 读一个整数
n = int(input())  # 等价于 in.nextInt()

# 2. 读一行用空格分隔的多个整数（最常见写法）
line = list(map(int, input().split()))
# input() 读入一行字符串，split() 按空格拆分，map(int, ...) 逐个转整数

# 3. 输出数组元素用空格分隔：等价于 System.out.print(nums[i] + " ")
nums = [1, 2, 3]
print(" ".join(map(str, nums)))  # 输出 "1 2 3"

# 4. 输出数组便于调试：等价于 Arrays.toString(nums)
print(nums)  # 直接输出 [1, 2, 3]
```

---

### 14. 方法签名与泛型列表 (List)

| 功能                     | Java 语法                                       | Python 3 语法                 |
| ------------------------ | ----------------------------------------------- | ----------------------------- |
| **定义方法**             | `public int twoSum(int[] nums, int target)`     | `def twoSum(nums, target):`   |
| **List 初始化**          | `List<Integer> ans = new ArrayList<>()`         | `ans = []`                    |
| **List 添加元素**        | `ans.add(x)`                                    | `ans.append(x)`               |
| **List 批量添加**        | `new ArrayList<>(Arrays.asList(a, b, c))`       | `ans.append([a, b, c])`       |
| **二维 List**            | `List<List<Integer>>`                           | 直接用嵌套列表 `[]`           |
| **返回数组**             | `return new int[]{a, b}`                        | `return [a, b]`               |
| **Map 的 values**        | `new ArrayList<>(hash.values())`                | `list(hash.values())`         |
| **Map 比较相等**         | `map1.equals(map2)`                             | `map1 == map2`                |

```python
# 1. 方法定义：Python 不需要类型声明，也不需要 public/private 修饰符
def twoSum(nums, target):
    return [0, 1]

# 2. 二维列表（结果收集）：等价于 List<List<Integer>> ans = new ArrayList<>()
ans = []
a, b, c = 1, 2, 3
ans.append([a, b, c])        # 等价于 ans.add(new ArrayList<>(Arrays.asList(a, b, c)))

# 3. 返回数组：等价于 return new int[]{a, b}
return [a, b]

# 4. 取 Map 的全部 value 组成列表：等价于 new ArrayList<>(hash.values())
result = list(hash_map.values())

# 5. 两个 HashMap 判断内容相等：等价于 map1.equals(map2)
if map1 == map2:
    print("相同")

# 6. 三目运算符：等价于 Java 的 条件 ? a : b
max_val = a if a > b else b
```

---

### 15. 高频陷阱速查表（结合本目录代码）

本目录的 Java 代码中反复出现以下写法，Python 翻译时极易踩坑：

| 陷阱                                    | Java 原文                                            | Python 正确写法                               |
| --------------------------------------- | ---------------------------------------------------- | --------------------------------------------- |
| **整数除法向下取整**                    | `int mid = left + (right - left) / 2;`               | `mid = left + (right - left) // 2`（`//` 才是整除）|
| **数组元素交换**                        | `swap(nums, i, j)` / `int t = a; a = b; b = t;`      | `nums[i], nums[j] = nums[j], nums[i]`（直接交换）|
| **字符串不可变需转列表**                | `StringBuilder sb; sb.setCharAt(i, c);`              | `sb = list(s); sb[i] = c; "".join(sb)`         |
| **for 循环多变量同时更新**              | `for (int i=0, j=0; ...; i++, j++)`                  | `while` 循环中手动 `i += 1; j += 1`            |
| **数组复制**                            | `int[] copy = nums.clone();`                         | `copy = nums[:]`（切片拷贝）                   |
| **增强 for 需要下标时**                 | `for (int i = 0; i < n; i++)`                        | `for i, num in enumerate(nums):`               |
| **判断字符串非空**                      | `!s.isEmpty()`                                       | `if s:`（空字符串为 False）                    |
| **取余结果为负数**（Python 与 Java 不同）| `-1 % 10` = `-1`                                     | Python 中 `-1 % 10` = `9`，需注意取模语义差异  |

```python
# 1. 二分查找取中间值：必须用 // 整数除法，否则得到浮点数会报错
mid = left + (right - left) // 2

# 2. 交换数组两个元素：Python 元组交换一步到位
nums[i], nums[j] = nums[j], nums[i]   # 等价于整个 swap 方法

# 3. 需要下标的同时遍历：等价于 Java 的普通 for 循环
for i, num in enumerate(nums):
    print(i, num)  # i 为下标，num 为元素

# 4. 字符串是不可变的，想要修改某个字符需先转列表再拼回
s = "hello"
sb = list(s)          # 等价于把字符串变成可变数组
sb[0] = "H"           # 等价于 sb.setCharAt(0, 'H')
s_new = "".join(sb)   # 结果为 "Hello"

# 5. 数组切片复制：等价于 nums.clone() 或 Arrays.copyOf
copy = nums[:]
```

---

### 16. 综合示例：一道题从 Java 翻译到 Python

以《两数之和_1》的哈希表解法为例，展示完整翻译思路：

```java
// ============ Java 原版 ============
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                return new int[]{map.get(target - nums[i]), i};
            }
            map.put(nums[i], i);
        }
        return null;
    }
}
```

```python
# ============ Python 翻译版 ============
def twoSum(nums, target):
    # 哈希表：存储「数值 -> 下标」的映射，等价于 HashMap<Integer, Integer> map
    hash_map = {}
    # 遍历数组：enumerate 同时拿到下标 i 和元素 num
    for i, num in enumerate(nums):
        # 判断 target - num 是否已经出现过，等价于 map.containsKey(target - num)
        if target - num in hash_map:
            # 返回两个下标组成的列表，等价于 return new int[]{...}
            return [hash_map[target - num], i]
        # 存入当前元素及其下标，等价于 map.put(num, i)
        hash_map[num] = i
    return None
```

再以《外观数列_38》为例，展示 StringBuilder 与 String 的翻译：

```java
// ============ Java 原版（片段） ============
StringBuilder sb = new StringBuilder();
sb.append(count).append(c);   // 连续追加 int 和 char，Java 会自动转字符串
// ...
return sb.toString();         // 转成 String
```

```python
# ============ Python 翻译版 ============
sb = []                        # 用列表代替 StringBuilder
sb.append(str(count))          # ⚠️ 必须手动转成字符串，Python 列表不会自动转
sb.append(c)
# ...
return "".join(sb)             # 等价于 sb.toString()
```

> **总结**：掌握「数组→列表、HashMap→dict、StringBuilder→list+join、栈→list、
> 队列→deque、for→range、i++→i+=1」这几个核心映射，就能顺畅地把本目录的
> Java 算法题翻译成 Python 复习了。建议逐题对照翻译，遇到不熟悉的语法随时查阅本文档。