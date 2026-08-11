num=int(input('Enter a three-digit number: '))
a=num//100
r_num=num%100
b=r_num//10
r_num=r_num%10
c=r_num

sum=a+b+c

print(f'Sum : {sum}')