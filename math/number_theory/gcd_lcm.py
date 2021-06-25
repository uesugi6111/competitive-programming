# a, bの最大公約数
def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)

# a, bの最小公倍数
def lcm(a, b):
    return (a * b) // gcd(a, b)

# 使用例
x, y = map(int, input().split())
print(gcd(x, y))
print(lcm(x, y))
