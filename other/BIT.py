# BinaryIndexedTree
class BinaryIndexedTree:
    def __init__(self, n):
        self.bit = [0] * n

    def add(self, i, x):
        i += 1
        while i <= len(self.bit):
            self.bit[i - 1] += x
            i += i & -i

    def sum_sub(self, i):
        a = 0
        while i:
            a += self.bit[i - 1]
            i -= i & -i
        return a

    def sum(self, i, j):
        return self.sum_sub(j) - self.sum_sub(i)

# 使用例:転倒数 https://atcoder.jp/contests/abc190/submissions/19857681
# 参考: https://scrapbox.io/pocala-kyopro/%E8%BB%A2%E5%80%92%E6%95%B0