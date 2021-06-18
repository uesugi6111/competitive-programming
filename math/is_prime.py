# 素数判定
def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# 使用例
n = int(input())
if is_prime(n):
    print("Yes")
else:
    print("No")
