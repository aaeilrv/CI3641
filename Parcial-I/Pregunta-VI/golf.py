import sys
from sympy import*
from math import log2,factorial as x
n=int(sys.argv[1])
print(fibonacci(floor(log2((x(n+1)//(x(n-1)*x(2)))+1))))