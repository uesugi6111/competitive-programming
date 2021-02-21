# めぐる式二分探索
def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    pass

def meguru_bisect(ng, ok):
    # 初期値の ng, ok を受け取り, is_ok を満たす最大(最小)の ok を返す
    # まず is_ok を定義する
    # ng, ok は とり得る最大の値 + 1, とり得る最小の値 - 1
    # 最小の ok を求める場合は ng, ok を逆にする
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
