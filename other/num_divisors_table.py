# 1からnまでの数のそれぞれの約数の個数(計算量O(nlogn))
# 長さnの配列を用意して1の倍数に+1、2の倍数に+1、3の倍数に+1、4の倍数に+1...と割り切れる数に足していく
def num_divisors_table(n):
    arr = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            arr[j] += 1
    return arr