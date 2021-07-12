# 座標圧縮
def compress(arr):
    *x, = set(arr)
    x.sort()
    return {e: i for i, e in enumerate(x)}

l=[15,0,15,30]
comp=compress(l) # {0:0,15:1,30:2}
ans=[] # 座標圧縮後の配列
for i in l:
    ans.append(comp[i])
print(ans) # [1,0,1,2]