a=int(input('s1='))
b=int(input('s2='))
c=int(input('s3='))

if((a+b>c)and(a+c>b)and(b+c>a)):
    print('Triangle is valid')
else:
    print('Triangle is not valid')
    