# 文字列の置換
s="abcabc"
print(s.replace("a","A")) # "AbcAbc"

# 文字列のソート
s="cdaeb"
print("".join(sorted(s))) # "abcde"

# 文字列を逆順に並び替える
s="abcde"
print(s[::-1]) # "edcba"

# 文字列を式として実行
s="2+3"
print(eval(s)) # 5