total=0
for i in range(1,6):
    age=int(input('Enter age of person:'))
    ticket=float(input('Enter ticket amount:'))

    if(age<12):
        ticket=ticket-(ticket*30/100)
    elif(age>59):
        ticket=ticket-(ticket*50/100)

    total=total+ticket
print(f'Total Ticket Amount = {total}')