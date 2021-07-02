# a ^ n % mod
def modpow(a, n, mod):
    if mod == 1:
        return 0
    res = 1
    while(n > 0):
        if (n & 1): res = res * a % mod  # n の最下位bitが 1 ならば a ^ (2 ^ i) をかける
        a = a * a % mod
        n >>= 1  # n を 1bit 右にシフトする
    return res

# 使用例
a, n = map(int, input().split())
mod = 10 ** 9 + 7
print(modpow(a, n, mod))
