# a ^ n % mod
a, n = map(int, input().split())
mod = 10 ** 9 + 7
print(pow(a, n, mod))
