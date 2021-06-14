# エラトステネスの篩
def eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
    return is_prime

# 使用例
x = int(input())
print(eratosthenes(x))
