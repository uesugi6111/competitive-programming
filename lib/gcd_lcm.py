# a, bの最大公約数
def gcd(a, b):
    if (a == 0): return b
    else: return gcd(b % a, a)

# a, bの最小公倍数
def lcm(a, b):
    return (a * b) // gcd(a, b)

# 使用例
a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))
