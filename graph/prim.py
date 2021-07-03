import heapq

n, m = map(int, input().split())  # 頂点数と辺数

# グラフ入力受け取り
graph = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())  # 頂点 a, b と辺の重み c
    graph[a].append((b, c))
    graph[b].append((a, c))

used = [False] * n  # used[i] : 頂点 i は既に使われたか記録
used_count = 0  # 既に使われた頂点の数

# 最初に頂点 0 を選ぶ
used[0] = True
used_count += 1

pos = []  # ヒープ

# 頂点 0 に隣接する辺を調べ, ヒープに追加
for (nv, c) in graph[0]:
    heapq.heappush(pos, (c, nv))  # (辺の重み, 頂点) として追加する

cost = 0  # 最小全域木の重みの合計

# プリム法
while used_count < n:
    c, v = heapq.heappop(pos)  # ヒープから最小の重みの辺を取り出す
    # 辺でつながっている頂点 v が既に使われていた場合は探索しない
    if used[v]:
        continue
    # 頂点 v を使ったことを記録
    used[v] = True
    used_count += 1
    # 使った辺の重みを足しておく
    cost += c
    # 新たに使った頂点 v に隣接する辺を調べる
    for (nv, c) in graph[v]:
        # 辺でつながっている頂点 nv が既に使われていた場合はヒープに追加しない
        if used[nv]:
            continue
        heapq.heappush(pos, (c, nv))

# 最小全域木の重みの合計
print(cost)
