e = input()
p = input()
is_v = ('@' in e and '.' in e) and (8 <= len(p) <= 16) and (e == e.lower())
print(is_v)