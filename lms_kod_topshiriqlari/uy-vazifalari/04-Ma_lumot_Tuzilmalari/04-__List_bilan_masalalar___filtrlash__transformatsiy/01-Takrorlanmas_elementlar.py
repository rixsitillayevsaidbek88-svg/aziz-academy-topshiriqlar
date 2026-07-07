elementlar = input().split()
takror = []
[takror.append(element) for element in elementlar if element not in takror]
print(' '.join(takror))