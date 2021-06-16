# 10 進数を x 進数に変換
def base_10_to_x(n, x):
    res = ""
    if n == 0:
        res = "0"
    else:
        while n > 0:
            c = str(n % x)
            res = c + res
            n //= x
    return res

# 使用例
n, x = map(int, input().split())
print(base_10_to_x(n, x))
