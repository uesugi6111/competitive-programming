# 高速素因数分解
from collections import Counter

class Osa_k:
    def __init__(self, n_max):
        self.is_prime = [True] * (n_max + 1)
        self.min_factor = [-1] * (n_max + 1)

        self.is_prime[0] = self.is_prime[1] = False
        self.min_factor[1] = 1

        # エラトステネスの篩
        for i in range(2, n_max + 1):
            if self.is_prime[i]:
                self.min_factor[i] = i
                for j in range(2 * i, n_max + 1, i):
                    self.is_prime[j] = False
                    if self.min_factor[j] == -1:
                        self.min_factor[j] = i
    
    def factorize(self, n):
        res = Counter()
        while n > 1:
            p = self.min_factor[n]
            exp = 0
            while self.min_factor[n] == p:
                n //= p
                exp += 1
            res[p] = exp
        return res

# 使用例
osa_k = Osa_k(100)
print(osa_k.factorize(10))  # Counter({2: 1, 5: 1})