S=int(input('Enter starting Number:'))
E=int(input("Enter ending number: "))

for i in range(S, E+1):
    if(i%5==0 and i%7==0):
        print(i)
