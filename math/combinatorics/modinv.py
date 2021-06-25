# 拡張ユークリッドの互除法
def ext_gcd(a, b):
    if b == 0:
        return (1, 0, a)
    else:
        (X, Y, g) = ext_gcd(b, a % b)
        return (Y, X - a // b * Y, g)

# mod m における a の逆元 (a と m が互いに素であることが必要)
# ax + my = 1 <=> ax ≡ 1(mod m)
def modinv(a, m):
    x, y, g = ext_gcd(a, m)
    return x % m

# 使用例
# a / b % mod = a * b ^ {-1} % mod
mod = 10 ** 9 + 7
a, b = map(int, input().split())
print(a * modinv(b, mod) % mod)
