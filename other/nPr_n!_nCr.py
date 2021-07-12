# 順列(nPr)
import itertools
l=["a","b","c"]
p=list(itertools.permutations(l,2)) # lから2個要素を選ぶ順列(第二引数を省略した場合、全ての要素を選ぶ順列、つまり階乗になる)
print(p) # [('a','b'),('a','c'),('b','a'),('b','c'),('c','a'),('c','b')]

# 順列(nPr)の総数
import math
def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

# 順列(n=r)の場合(つまり階乗n!)
import itertools
n=int(input())
factorial=list(itertools.permutations(list(range(1,n+1)))) # n!通りの順列が含まれるリスト
print(factorial) # リストのそれぞれの要素はタプルであることに注意！

# 組み合わせ(nCr)
import itertools
l=["a","b","c"]
c=list(itertools.combinations(l,2)) # lから2個要素を選ぶ組み合わせ
print(c) # [('a','b'),('a','c'),('b','c')]

# 組み合わせ(nCr)の総数
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

# 重複組み合わせ
# nHr = n+r−1Cr