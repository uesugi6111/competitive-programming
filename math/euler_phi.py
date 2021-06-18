# オイラーの φ 関数
def euler_phi(n):
    res = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            res = res // i * (i - 1)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        res = res // n * (n - 1)
    return res

# 使用例
n = int(input())
print(euler_phi(n))
