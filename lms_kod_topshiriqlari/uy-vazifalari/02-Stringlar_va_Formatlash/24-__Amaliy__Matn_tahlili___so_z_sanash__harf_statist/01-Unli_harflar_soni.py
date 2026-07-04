a = input()
unli = 'aeiou'
a = a.lower()
unli_son = 0
for harf in a:
    if harf in unli:
        unli_son += 1
print(unli_son)