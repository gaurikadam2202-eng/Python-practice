length=float(input('Enter the Length:'))
breadth=float(input('Enter the Breadth:'))
radius=float(input('Enter the Radius:'))

areaR=length*breadth
areaSC=3.14*radius**2/2

area=areaR+areaSC

primeter=(2*length)+breadth+(3.14*radius)

print(f'Area={area}')
print(f'Primeter={primeter}')
