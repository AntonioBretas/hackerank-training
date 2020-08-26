import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    # .strip() remove espaços em brando a direita e esquerda

n1 = n%2 # % resto de divisão

if n1==0:  # caso o resto da divisão por 2 seja 0 o número é par
    if n>=2 and n<=5:
        print(f"Not Weird")
    elif n>=6 and n<=20:
        print(f"Weird")
    elif n>20:
        print(f"Not Weird")
else:
    print(f"Weird")
