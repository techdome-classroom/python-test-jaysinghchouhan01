def decode_message( s: str, p: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(p):
        if p[j] == '*':
            j += 1
            while j < len(p) and p[j] == '*':
                j += 1
            if j == len(p):
                return True
            while i < len(s) and (s[i] != p[j] or p[j] == '?'):
                i += 1
        elif p[j] == '?':
            i += 1
            j += 1
        elif s[i] == p[j]:
            i += 1
            j += 1
        else:
            return False
    return i == len(s) and j == len(p)
