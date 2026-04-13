def solve(s):
    seen = {}
    left = 0
    res = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        res = max(res, right - left + 1)
    return res

print(solve("abcabcbb"))
