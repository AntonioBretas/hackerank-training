import re
value = input()
n1 = '\n' #Variável para usaliza \n na f-string
c = '[qwrtypsdfghjklzxcvbnm]'
m = re.findall(r'(?<='+ c +')([aeiou]{2,})'+ c, value, re.I)#re.I serve pra utlizar letrar maiúsculas e minúsculas

print(f"{n1.join(m or ['-1'])}")#f-string não aceita \


#import re
#value = input()
#c = '[qwrtypsdfghjklzxcvbnm]'
#x = r'(?<='+ c +')([aeiouAEIOU]{2,})'+ c
#d = re.compile(x)
#m = d.findall(value)

#print('\n'.join(m or ['-1']))
