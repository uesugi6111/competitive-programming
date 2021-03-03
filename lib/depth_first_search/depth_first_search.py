# 深さ優先探索
def depth_first_search(g, s, v):
    s[v] = True  # v を訪問済みとする
    for nv in g[v]:
        if s[nv]: continue  # 既に訪問済みの頂点は探索しない
        depth_first_search(g, s, nv)  # 再帰的に探索


n, m = map(int, input().split())  # 頂点数と辺数

# グラフ入力受け取り (ここでは無向グラフを想定)
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

seen = [False] * n  # 全頂点を False(未訪問) に初期化

depth_first_search(graph, seen, 0)  # 頂点 0 をスタートとした探索
