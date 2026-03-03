import re

S = input()
P = input()
R = input()

print(re.sub(re.escape(P), R, S))