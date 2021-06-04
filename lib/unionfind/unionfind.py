# UnionFindTree
class UnionFind:
    def __init__(self, n):
        self.p = [-1] * n  # parent
        self.r = [1] * n  # rank
    def find(self, x):
        if self.p[x] == -1:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.r[x] > self.r[y]:
            x, y = y, x
        if self.r[x] == self.r[y]:
            self.r[y] += 1
        self.p[x] = y
    def same(self, x, y):
        return self.find(x) == self.find(y)

# 使用例
n, q = map(int, input().split())
uf = UnionFind(n)
for i in range(q):
    p, a, b = map(int,input().split())
    if p == 0:
        uf.unite(a, b)
    else:
        if uf.same(a, b):
            print("Yes")
        else:
            print("No")
