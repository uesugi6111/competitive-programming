# Binary Indexed Tree (Fenwick Tree)
class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    # v[i] += x, i is 0-indexed
    def add(self, i, x):
        i += 1
        while i <= self.n:
            self.tree[i] += x
            i += i & -i
    
    # v[0] + ... + v[i], i is 0-indexed
    def sum(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

# 使用例
n, q = map(int, input().split())
bit = BIT(n)
a = list(map(int, input().split()))
for i in range(n):
    bit.add(i, a[i])
for i in range(q):
    com, a, b = list(map(int, input().split()))
    if com == 0:
        bit.add(a, b)
    else:
        print(bit.sum(b - 1) - bit.sum(a - 1))