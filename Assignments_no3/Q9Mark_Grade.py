s1=int(input('First Sub Mark:'))
s2=int(input('Second Sub Mark: '))
s3=int(input('Third Sub Mark: '))
s4=int(input('Forth Sub Mark: '))
s5=int(input('Fifth Sub Mark: '))

TotalMark= s1+s2+s3+s4+s5
print(f'TotalMark={TotalMark}')

P=(TotalMark/500)*100

print(f'Percentage={P}')

if(P>=85):
    print('First class A Grade')
elif(P>=65):
    print('Second class B Grade')
elif(P>=45):
    print('Third class C Grade')
elif(P>=35):
    print('Forth class D Grade')
else:
    print('fail')
