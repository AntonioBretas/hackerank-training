import re
value = str(input())
regex = r'([a-zA-Z0-9])\1+'
m = re.search(regex, value)
if not m:
    print("-1")
else:
    print(m.group(1))
