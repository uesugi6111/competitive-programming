# UnionFind(https://tumoiyorozu.github.io/single-file-ac-library/document_ja/dsu.htmlを参照)
class UnionFind:
    from typing import List, Set
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n
    def merge(self, x, y) -> int:
        x = self.leader(x)
        y = self.leader(y)
        if x == y:
            return 0
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return self.parent[x]
    def same(self, x, y) -> bool:
        return self.leader(x) == self.leader(y)
    def leader(self, x) -> int:
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.leader(self.parent[x])
            return self.parent[x]
    def size(self, x) -> int:
        return -self.parent[self.leader(x)]
    def groups(self) -> List[Set[int]]:
        groups = dict()
        for i in range(self.n):
            p = self.leader(i)
            if not groups.get(p):
                groups[p] = set()
            groups[p].add(i)
        return list(groups.values())

n,m=map(int,input().split())
uf=UnionFind(n) # n頂点0辺の無向グラフを作成
for i in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    uf.merge(a,b) # 辺(a,b)を足す
print(uf.groups()) # グラフを連結成分に分け、その情報を出力