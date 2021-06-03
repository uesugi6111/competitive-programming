from collections import deque

n, m = map(int, input().split())  # 頂点数と辺数

# グラフ入力受け取り (ここでは無向グラフを想定)
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * n  # 全頂点を -1(未訪問) に初期化
pos = deque()  # キュー

# 初期条件 (頂点 0 を初期ノードとする)
dist[0] = 0
pos.append(0)

# 幅優先探索 (キューが空になるまで探索を行う)
while len(pos) > 0:
    v = pos.popleft()  # キューから先頭の頂点を取り出す
    for nv in graph[v]:
        # 既に訪問済みの頂点は探索しない
        if dist[nv] != -1:
            continue
        # 新たな頂点 nv について距離情報を更新してキューに追加する
        dist[nv] = dist[v] + 1
        pos.append(nv)

# 結果出力 (各頂点の頂点 0 からの距離)
for v in range(n):
    print("{0} : {1}".format(v, dist[v]))
