Cp=int(input('Cost Price : '))
Sp=int(input('Sellig Price : '))

if(Sp>Cp):
    print('Profit')
elif(Cp>Sp):
    print('Loss')
else:
    print('No Profit & No Loss')
