import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

n1 = n%2

if n1==0:
    if n>=2 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")
else:
    print("Weird")
