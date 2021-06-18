def is_ok(n):
    # 条件を満たすか？問題ごとに定義する
    pass

# 二分探索
def binary_search(ok, ng):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
