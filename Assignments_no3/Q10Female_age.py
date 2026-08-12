G=input('Enter Gender M/F:')
A=int(input('Enter Age: '))
if(G=='F'):
    if(A>=18):
        print('Girl is eligible for marriage.')
    else:
        print('Girl is not eligible for marriage.')
else:
    if(A>=21):
        print('Boy is eligible for marriage.')
    else:
        print('Boy is not eligible for marriage')


