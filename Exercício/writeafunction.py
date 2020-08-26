def is_leap(year): #def define funções onde terá uma sequência de comandos
    leap = False
    
    if year%4==0 and year%100!=0 or year%400==0:
        leap = True
    
    return leap # retorna o valor de leap para a variável

year = int(input())
print(is_leap(year))
