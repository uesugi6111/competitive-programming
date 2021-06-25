# nCk % mod
mx = 5 * 10 ** 5
mod = 10 ** 9 + 7  # mod は素数であることが必要

fac = [0] * (mx + 1)  # fac[i] : i! % mod
finv = [0] * (mx + 1)  # finv[i] : fac[i] の逆元
inv = [0] * (mx + 1)  # inv[i] : i の逆元

# 前計算
def init():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, mx + 1):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod

# 二項係数を計算
def comb_mod(n, k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod

# 使用例
n, k = map(int, input().split())
init()
print(comb_mod(n, k))