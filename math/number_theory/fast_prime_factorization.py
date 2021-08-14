from collections import Counter

class Eratosthenes:
    def __init__(self, n_max):
        self.is_prime = [True] * (n_max + 1)  # 整数 i が素数であるかどうか
        self.min_factor = [-1] * (n_max + 1)  # 整数 i を割り切る最小の素数
        self.mobius = [1] * (n_max + 1)  # メビウス関数値

        self.is_prime[0] = self.is_prime[1] = False
        self.min_factor[1] = 1

        # エラトステネスの篩
        for i in range(2, n_max + 1):
            if self.is_prime[i]:
                self.min_factor[i] = i
                self.mobius[i] = -1
                for j in range(2 * i, n_max + 1, i):
                    self.is_prime[j] = False
                    if self.min_factor[j] == -1:
                        self.min_factor[j] = i
                    if (j // i) % i == 0:  # j が i で 2 回以上割り切れる場合
                        self.mobius[j] = 0
                    else:
                        self.mobius[j] = -self.mobius[j]
    
    # 高速素因数分解 (osa_k 法)
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
    
    # 高速約数列挙
    def divisors(self, n):
        res = [1]
        pf = self.factorize(n)
        for p in pf.keys():
            size = len(res)
            for i in range(size):
                x = 1
                for j in range(pf[p]):
                    x *= p
                    res.append(res[i] * x)
        res.sort()
        return res

# 使用例
er = Eratosthenes(100)

# 素因数分解
print(er.factorize(10))  # Counter({2: 1, 5: 1})

# 約数列挙
print(er.divisors(10))  # [1, 2, 5, 10]