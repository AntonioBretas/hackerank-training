import re
s = input()
k = re.compile(input())#compile junta RE ao objeto facilitando busca
m = k.search(s)
if not m:
    print ((-1, -1))
while m:
    print ((m.start(), m.end()-1))
    #print ("({0}, {1})".format(m.start(), m.end()-1))
    m = k.search(s,m.start()+1)
