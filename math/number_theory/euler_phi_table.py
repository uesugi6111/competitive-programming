# オイラーの φ 関数テーブル
def euler_phi_table(n):
    euler = list(range(n + 1))
    for i in range(2, n + 1):
        if euler[i] == i:
            for j in range(i, n + 1, i):
                euler[j] = euler[j] // i * (i - 1)
    return euler

# 使用例
n = int(input())
print(euler_phi_table(n))
