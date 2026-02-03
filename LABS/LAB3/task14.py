n = int(input())
a = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    parts = input().split()
    op = parts[0]
    if op == "add":
        x = int(parts[1])
        a = list(map(lambda v, x=x: v + x, a))
    elif op == "multiply":
        x = int(parts[1])
        a = list(map(lambda v, x=x: v * x, a))
    elif op == "power":
        x = int(parts[1])
        a = list(map(lambda v, x=x: v ** x, a))
    else:  # abs
        a = list(map(lambda v: abs(v), a))

print(*a)