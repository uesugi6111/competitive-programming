# 素因数分解
def prime_factorization(n):
    i = 2
    arr = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            arr.append(i)
        i += 1
    if n > 1:
        arr.append(n)
    return arr

# 使用例
n = int(input())
res = prime_factorization(n)
print(res)
from collections import Counter
print(Counter(res))  # Counter({素因数 : 指数, ...})