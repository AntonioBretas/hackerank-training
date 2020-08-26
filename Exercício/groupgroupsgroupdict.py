import re
value = str(input())
regex = r'([a-zA-Z0-9])\1+'
m = re.search(regex, value)
if not m:
    print(f"-1")
else:
    print(f"{m.group(1)}")
