s = input()
count = 0

for ch in s:
    if 'A' <= ch <= 'Z':
        count += 1

print(count)