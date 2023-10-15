import sys
from sympy import*
print(fibonacci(floor(log(bell(int(sys.argv[1])+1),2))+1))