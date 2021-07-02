n, m = map(int, input().split())  # 頂点数と辺数

INF = 10 ** 18
dist = [[INF] * n for _ in range(n)]  # dist[i][j] : 頂点 i から頂点 j への最短距離

# 同じ頂点同士の距離は 0 とする
for i in range(n):
    dist[i][i] = 0

# グラフ入力受け取り (ここでは無向グラフを想定)
for i in range(m):
    a, b, c = map(int, input().split())  # 頂点 a, b と辺の重み c
    dist[a][b] = c
    dist[b][a] = c

# ワーシャル‐フロイド法
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] != INF and dist[k][j] != INF:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 負閉路判定
def is_negative():
    for i in range(n):
        if dist[i][i] < 0:
            return True
    return False
