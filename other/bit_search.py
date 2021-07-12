# bit全探索(itertools使用)
from itertools import product
n=int(input())
l=list(product([0,1],repeat=n))
print(l) # 入力:2 出力:[(0, 0), (0, 1), (1, 0), (1, 1)]