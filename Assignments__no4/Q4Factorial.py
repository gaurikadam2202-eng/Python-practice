num= int(input('Enter Number:'))
factorial=1
for i in range(num,0,-1):
    factorial=factorial*i

print(f'factorial = {factorial}')