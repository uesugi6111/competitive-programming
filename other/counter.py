# 配列の各要素の出現個数をカウント
from collections import Counter
l=["1","2","3","1"]
c=Counter(l)
print(c) # Counter({'1':2,'2':1,'3':1})
print(c["1"]) # 2
print(c["2"]) # 1
print(c["3"]) # 1
print(c["4"]) # 0　存在しないものを指定した場合は0
print(c.most_common()) # [('1',2),('2',1),('3',1)]　Counterを配列(1つ1つの要素はタプル)に変換