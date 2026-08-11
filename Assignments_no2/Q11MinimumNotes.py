Amount=int(input('Enter Amount='))
notes_2000=Amount//2000
r_amount=Amount%2000
notes_500=r_amount//500
r_amount=r_amount%500
notes_100=r_amount//100
r_amount=r_amount%100
notes_50=r_amount//50
r_amount=r_amount%50
notes_10=r_amount//10
r_amount=r_amount%10

print(f'Notes of 2000 = {notes_2000}')
print(f'Notes of 500 = {notes_500}')
print(f'Notes of 100 ={notes_100}')
print(f'Notes of 50 ={notes_50}')
print(f'Notes of 10 ={notes_10}')
print(f'Remaining Amount = {r_amount}')