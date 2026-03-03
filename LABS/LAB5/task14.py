import re

s = input().strip()
p = re.compile(r'^\d+$')

print("Match" if p.match(s) else "No match")