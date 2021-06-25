# 拡張ユークリッドの互除法
# ax + by = gcd(a, b) となるような x, y を求める (x, y は |x| + |y| が最小のもの)
# 戻り値は (x, y, gcd(a, b))
def ext_gcd(a, b):
    if b == 0:
        return (1, 0, a)
    else:
        (X, Y, g) = ext_gcd(b, a % b)
        return (Y, X - a // b * Y, g)

# 使用例
a, b = map(int, input().split())
x, y, g = ext_gcd(a, b)
print(x, y)
