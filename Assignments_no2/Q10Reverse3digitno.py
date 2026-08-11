num=int(input('Enter the three digit no :'))

a=num%10

b=(num//10)%10

c=num//100

print(f'a= {a}')
print(f'b= {b}')
print(f'c= {c}')

reverse = a*100+b*10+c

print(f'Reverse Number = {reverse}')