# x, yの最大公約数
def gcd(x, y):
    if (y == 0):
        return x
    else:
        return gcd(y, x % y)

# x, yの最小公倍数
def lcm(x, y):
    return (x * y) // gcd(x, y)

# 使用例
a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))
