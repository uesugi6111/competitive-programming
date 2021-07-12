# deque(データの追加を先頭、末尾両方に対してO(1)のコストで行える。)
# (通常のlistだと先頭に追加する場合にO(n)のコストがかかる。)
from collections import deque

d = deque('a') # deque(['a'])
d.append('b') # 末尾に要素を追加　deque(['a', 'b'])
d.appendleft('c') # 先頭に要素を追加　deque(['c', 'a', 'b'])

print(d) # deque(['c', 'a', 'b'])

print(list(d)) # ['c', 'a', 'b']

print(''.join(d)) # cab