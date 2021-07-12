# 切り捨て
# floor(a/b)=(a-(a%b))//b
a=int(input())
b=int(input())
print(a//b)

# 切り上げ
from math import ceil
a=int(input())
b=int(input())
print(ceil(a/b))

# 階乗
from math import factorial
print(factorial(0)) # 0!=1
print(factorial(5)) # 5!=120