if __name__ == '__main__':
    n = int(input())

x = range (1, n+1) # cria uma sequência de números de 1 até n+1
#range(começo,fim,passos)

for i in x:
    print (f'{i}',end="")
    # end="" faz todos valores sairem na mesma linha
    # end="" não funciona dentro da f-string
