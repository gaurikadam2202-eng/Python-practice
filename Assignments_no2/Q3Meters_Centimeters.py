feet=float(input('Enter feet :'))
inch=float(input('Enter inch: '))
Meters=(feet*0.3048)+(inch*0.0254)
Centimeters=Meters*100
print(f'Distance in Meters:{Meters}')
print(f'Distance in Centimeters:{Centimeters}')