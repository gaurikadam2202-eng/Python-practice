num=int(input('Enter Number:'))
count=len(str(num))
temp=num
sum=0
while num>0:
    dig=num%10
    sum=sum+(dig**count)
    num//=10
if(temp==sum):
    print(f'{temp} is Armstrong Number')
else:
    print(f'{temp} is Not Armstrong Number')