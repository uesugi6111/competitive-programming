# 約数列挙
def divisors(n):
    arr = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            arr.append(i)
            if n // i != i:
                arr.append(n // i)
        i += 1
    arr.sort()
    return arr

# 使用例
n = int(input())
print(divisors(n))
