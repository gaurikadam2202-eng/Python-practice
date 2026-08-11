Days=int(input('Enter the Number of days:'))

Years= Days // 365

remaning_days = Days % 365

Week = remaning_days // 7

remaning_days = remaning_days % 7

print(f'Years : {Years}')
print(f'Week : {Week}')
print(f'Days : {remaning_days}')
