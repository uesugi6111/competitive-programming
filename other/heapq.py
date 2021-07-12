# 優先度付きキュー

# できること
# リストのヒープ化　O(N)
# 要素の追加　O(logN)
# 最小値の取得(つまり要素の削除)　O(logN)

# 例:最小値の取得
import heapq

l=[2,4,5]
heapq.heapify(l)  # リストlを優先度付きキューに変換
print(l)

heapq.heappush(l,1)  # 要素の追加
print(l)

print(heapq.heappop(l))  # 最小値の取得と表示
print(l)

# 例:最大値の取得
# あらかじめ各要素を-1倍しておく．最小値を取得し，それを-1倍した値が最大値である．
import heapq

l=[2,4,5]
l=list(map(lambda x:x*(-1),l))  # 各要素を-1倍
heapq.heapify(l)  # リストlを優先度付きキューに変換
print(l)

heapq.heappush(l,1*(-1))  # 要素の追加
print(l)

print(heapq.heappop(l)*(-1))  # 最大値の取得と表示
print(l)