# 座標圧縮
def compression(arr):
    return {e : i for i, e in enumerate(sorted(set(arr)))}

# 使用例
l = [15, 0, 15, 30]
comp = compression(l)  # {0 : 0, 15 : 1, 30 : 2}
res = []  # 座標圧縮後の配列
for i in l:
    res.append(comp[i])
print(res)  # [1, 0, 1, 2]