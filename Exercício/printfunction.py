if __name__ == '__main__':
    n = int(input())

x = range (1, n+1)

for i in x:
    print (f'{i}',end="")
    # end="" faz todos valores sairem na mesma linha
    # end="" não funciona dentro da f-string
