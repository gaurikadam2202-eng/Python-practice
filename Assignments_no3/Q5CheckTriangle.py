a=int(input('First side:'))
b=int(input('Second side: '))
c=int(input('Third side:'))

if(a==b==c):
    print('Triangle is equilateral triangle')
elif(a==b or a==c or b==c):
    print('Triangle is isoscaler triangle')
else:
    print('Triangle is scalene triangle')