# ランレングス圧縮
def rle(s):
    res = ""
    i = 0
    while i < len(s):
        startpos = i
        while i < len(s) and s[startpos] == s[i]:
            i += 1
        res += s[startpos]
        res += str(i - startpos)
    return res

# 使用例
s = input()
print(rle(s))
