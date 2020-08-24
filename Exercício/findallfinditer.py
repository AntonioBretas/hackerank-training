import re
value = input()
c = '[qwrtypsdfghjklzxcvbnm]'
m = re.findall(r'(?<='+ c +')([aeiou]{2,})'+ c, value, re.I)

print('\n'.join(m or ['-1']))
