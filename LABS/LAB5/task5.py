import re

s = input()
print("Yes" if re.search(r'^[A-Za-z].*\d$', s) else "No")