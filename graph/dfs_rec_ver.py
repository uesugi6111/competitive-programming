# 再帰上限を増やす
import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())  # 頂点数と辺数

# グラフ入力受け取り (ここでは無向グラフを想定)
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n  # 全頂点を False(未訪問) に初期化

# 深さ優先探索
def dfs(v):
    visited[v] = True  # v を訪問済みとする
    for nv in graph[v]:
        # 既に訪問済みの頂点は探索しない
        if visited[nv]:
            continue
        dfs(nv)  # 再帰的に探索

dfs(0)  # 頂点 0 をスタートとした探索
