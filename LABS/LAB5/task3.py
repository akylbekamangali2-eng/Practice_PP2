import re

S = input()
P = input()

print(len(re.findall(re.escape(P), S)))