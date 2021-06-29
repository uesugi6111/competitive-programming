n, m = map(int, input().split())  # 頂点数と辺数

# グラフ入力受け取り (ここでは無向グラフを想定)
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n  # 全頂点を False (未訪問) に初期化
pos = []  # スタック

# 初期条件 (頂点 0 を始点とする)
pos.append(0)

# 深さ優先探索 (スタックが空になるまで探索を行う)
while len(pos) > 0:
    v = pos.pop()  # スタックから末尾の頂点を取り出す
    visited[v] = True  # v を訪問済みとする
    for nv in graph[v]:
        # 既に訪問済みの頂点は探索しない
        if visited[nv]:
            continue
        # 新たな頂点 nv をスタックに追加する
        pos.append(nv)
