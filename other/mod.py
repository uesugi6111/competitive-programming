# a ^ n % mod
a, n = map(int, input().split())
mod = 10 ** 9 + 7
print(pow(a, n, mod))


# nCk % mod
def comb_mod(n,k,p):
  a,b=1,1
  k=min(k,n-k)
  for i in range(k):
    a=a*(n-i)%p
    b=b*(k-i)%p
  return a*pow(b,p-2,p)%p

n,k=map(int,input().split())
mod=10**9+7
print(comb_mod(n,k,mod))


# mod. m での a の逆元 a^{-1} を計算する(計算量O(logm))
def modinv(a, m):
    b, u, v = m, 1, 0
    while(b):
        t = a // b
        a -= t * b; a, b = b, a
        u -= t * v; u, v = v, u
    u %= m
    if (u < 0): u += m
    return u

# 使用例
# a / b % mod
# = a * b^{-1} % mod

a, b = map(int, input().split())
mod = 10 ** 9 + 7
print(a % mod * modinv(b, mod) % mod)