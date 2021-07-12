# しゃくとり法

# 例:総和がk以下となる区間を数え上げ
n,k=map(int,input().split())
l=list(map(int,input().split()))
right,s,ans=0,0,0
for left in range(n):
    while right<n and s+l[right]<=k:  # right<n かつ rightを進めてよい条件
        # 実際にrightを1進める
        s+=l[right]
        right+=1

    # breakした状態でrightは条件を満たす最大なので，何かする
    ans += right-left

    # leftをインクリメントする準備
    if right==left: right+=1
    else: s-=l[left]
print(ans)