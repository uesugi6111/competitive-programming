# 2次元累積和
def cumulative_sum_2d(arr):
    # cumsum_2d[i][j] = [0, i) * [0, j) の総和
    h = len(arr)
    w = len(arr[0])
    cumsum_2d = [[0] * (w + 1) for i in range(h + 1)]
    for i in range(h):
        for j in range(w):
            cumsum_2d[i + 1][j + 1] = cumsum_2d[i + 1][j] + cumsum_2d[i][j + 1] - cumsum_2d[i][j] + arr[i][j]
    return cumsum_2d

# 使用例
h, w = map(int, input().split())
l = [list(map(int,input().split())) for i in range(h)]
cumsum = cumulative_sum_2d(l)
h1, h2, w1, w2 = map(int,input().split())
print(cumsum[h2][w2] - cumsum[h1][w2] - cumsum[h2][w1] + cumsum[h1][w1])  # [h1, h2) * [w1, w2) の総和
