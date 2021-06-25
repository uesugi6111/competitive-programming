# 逆元列挙
mx = 5 * 10 ** 5
mod = 10 ** 9 + 7  # mod は素数であることが必要
inv = [0] * (mx + 1)  # inv[i] : i の逆元
inv[1] = 1
for i in range(2, mx + 1):
    # mod // i * i + mod % i = mod
    # mod // i * i + mod % i ≡ 0
    # mod // i * i ≡ -mod % i
    # mod // i * -inv(mod % i) ≡ inv(i)
    inv[i] = mod // i * -inv[mod % i]
    if inv[i] < 0: inv[i] += mod
