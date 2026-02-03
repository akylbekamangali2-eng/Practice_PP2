s = input().strip()

digits = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
}

rev_digits = {
    "0": "ZER", "1": "ONE", "2": "TWO", "3": "THR", "4": "FOU",
    "5": "FIV", "6": "SIX", "7": "SEV", "8": "EIG", "9": "NIN"
}

expr = ""
i = 0

while i < len(s):
    if s[i] in "+-*":
        expr += s[i]
        i += 1
    else:
        part = s[i:i+3]
        expr += digits[part]
        i += 3

result = eval(expr)

if result == 0:
    print("ZER")
else:
    ans = ""
    for d in str(result):
        ans += rev_digits[d]
    print(ans)