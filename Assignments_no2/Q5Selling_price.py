Cost_Price=int(input('Enter Cost Price:'))
Discount=int(input('Enter Discount Percentage:'))

Discount=(Cost_Price*Discount)/100
Selling_Price=Cost_Price-Discount

print(f'Discount = {Discount}')
print(f'Selling price = {Selling_Price}')