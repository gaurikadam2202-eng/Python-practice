S=int(input('Enter starting Number:'))
E=int(input("Enter ending number: "))
n = int(input("Enter divisor:"))
for i in range(S,E+1):
    if(i%n==0):
        print(i)

    