num=int(input('Enter 3 digit number: '))
temp=num
rev=0
while(temp>0):
    digit=temp%10
    temp//=10
    rev=rev*10+digit
if(rev==num):
    print(f'{num} is pallindrom number')
else:
    print(f'{num} is not pallindrom number')
