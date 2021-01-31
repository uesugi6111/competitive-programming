# a ^ n % mod
def modpow(a, n, mod):
    return pow(a, n, mod)

a, n = map(int, input().split())
mod = 10 ** 9 + 7
print(modpow(a, n, mod))
