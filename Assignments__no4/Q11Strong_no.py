num=int(input('Enter Number:'))
temp=num
sum=0
while(num>0):
    digit=num%10
    fact=1
    for i in range(1, digit+1):
        fact=fact*i
    sum=sum+fact
    num//=10
if(temp==sum):
        print(f'{temp} is Strong Number')
else:
        print(f'{temp} is not Strong Number')
    
