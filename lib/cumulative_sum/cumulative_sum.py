# 累積和
def cumulative_sum(arr):
    n = len(arr)
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + arr[i]
    return s


# 使用例
l = list(map(int, input().split()))
cumsum = cumulative_sum(l)  # 累積和
left, right = map(int, input().split())
print(cumsum[right] - cumsum[left])  # 区間 [left, right) の総和
