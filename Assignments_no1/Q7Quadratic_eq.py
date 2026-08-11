import math
a=int(input('Enter the value of a: '))
b=int(input('Enter the value of b: '))
c=int(input('Enter the value of c: '))
d=b**2-4*a*c

x1=(-b + (d**0.5)) /2*a
x2=(-b - (d**0.5)) /2*a
print(f'value of D is {d}')
print(f'value of first root is {x1}')
print(f'value of second root is {x2}')