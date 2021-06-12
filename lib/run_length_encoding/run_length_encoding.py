# ランレングス圧縮
def rle(s):
    res = ""
    length = len(s)
    i = 0
    while i < length:
        startpos = i
        while i < length and s[startpos] == s[i]:
            i += 1
        res += s[startpos]
        res += str(i - startpos)
    return res


# 使用例
s = input()
print(rle(s))
