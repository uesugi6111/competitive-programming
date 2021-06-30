import heapq

n, m = map(int, input().split())  # 頂点数と辺数

# グラフ入力受け取り (ここでは無向グラフを想定)
graph = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())  # 頂点 a, b と辺の重み c
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [-1] * n  # 全頂点を -1 (未訪問) に初期化

pos = []  # ヒープ
done = [False] * n  # ヒープから 1 度でも取り出したことがあるか記録

# 初期条件 (頂点 0 を始点とする)
dist[0] = 0
heapq.heappush(pos, (0, 0))  # (距離, 頂点) として追加する

# ダイクストラ法（ヒープが空になるまで探索を行う）
while len(pos) > 0:
    d, v = heapq.heappop(pos)  # ヒープから先頭の頂点を取り出す
    # 既にヒープから取り出したことのある頂点は探索しない
    if done[v]:
        continue
    done[v] = True  # ヒープから取り出したことを記録
    for (nv, c) in graph[v]:
        # 未訪問のとき, または最短距離が更新可能なとき
        if dist[nv] == -1 or dist[nv] > dist[v] + c:
            # 新たな頂点 nv について距離情報を更新してヒープに追加する
            dist[nv] = dist[v] + c
            heapq.heappush(pos, (dist[nv], nv))

# 結果出力 (各頂点の頂点 0 からの距離)
for v in range(n):
    print("{0} : {1}".format(v, dist[v]))
