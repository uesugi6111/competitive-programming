# リストをNumPy配列ndarrayに変換
import numpy as np
l_1d = [0, 1, 2]
arr_1d = np.array(l_1d)
print(arr_1d)
# [0 1 2]

# NumPy配列ndarrayをリストに変換
import numpy as np
arr_1d = np.arange(3)
print(arr_1d)
# [0 1 2]
print(arr_1d.tolist())
# [0, 1, 2]

# 2次元配列の回転
import numpy as np
a_2d = np.arange(6).reshape(2, 3)
print(a_2d)
# [[0 1 2]
#  [3 4 5]]

# 反時計回りに90度回転
print(np.rot90(a_2d))
# [[2 5]
#  [1 4]
#  [0 3]]

# 反時計回りに180度回転
print(np.rot90(a_2d, 2))
# [[5 4 3]
#  [2 1 0]]

# 反時計回りに270度回転
print(np.rot90(a_2d, 3))
# [[3 0]
#  [4 1]
#  [5 2]]

# 時計回りに90度回転
print(np.rot90(a_2d, -1))
# [[3 0]
#  [4 1]
#  [5 2]]